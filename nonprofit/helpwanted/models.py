from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.utils import timezone
import datetime

POSITION_TYPE_CHOICES = (
    ('ft', 'Full-time'),
    ('pt', 'Part-time'),
    ('i', 'Internship'),
    ('fl', 'Freelance'),
)

JOBS_NEW_THRESHOLD = getattr(settings, 'JOBS_NEW_THRESHOLD', 14)


class JobListingManager(models.Manager):
    def open(self, is_filled=False):
        now = timezone.now()
        jobs = JobListing.objects.filter(published_until__gte=now, is_filled=is_filled)
        return jobs


class JobListing(models.Model):
    objects = JobListingManager()
    position = models.CharField("Position title", max_length=255)
    position_type = models.CharField("Type of employment",  max_length=2, choices=POSITION_TYPE_CHOICES)
    position_description = models.TextField("Description of the position")
    organization = models.CharField("Name of employer", max_length=255)
    organization_url = models.URLField("URL of employer", blank=True, null=True)
    location = models.CharField("Location of job opportunity", max_length=255)

    contact_name = models.CharField("Name of organizational contact", max_length=255)
    contact_email = models.EmailField("Contact email")
    contact_phone = models.CharField("Contact phone number", max_length=32, blank=True, null=True)

    is_filled = models.BooleanField(default=False)

    date_published = models.DateTimeField(blank=True)
    published_until = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-date_published', 'position']

    def __unicode__(self):
        return self.position

    def save(self):
        if not self.pk:
            self.date_published = timezone.now()
        if not self.published_until:
            self.published_until = self.date_published + datetime.timedelta(30)
        super(JobListing, self).save()

    @permalink
    def get_absolute_url(self):
        return ('job_detail', [str(self.pk)])

    def is_expired(self):
        return timezone.now() > self.published_until

    def is_new(self):
        delta = timezone.now() - self.date_published
        return delta.days < JOBS_NEW_THRESHOLD
