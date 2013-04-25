from django.db import models
import uuid

EMPLOYMENT_STATUSES = (
    ('ft', 'Full Time'),
    ('pt', 'Part Time'),
    ('i', 'Internship'),
    ('f', 'Fellowship'),
    ('c', 'Consultant'),
    ('v', 'Volunteer'),
    ('ex', 'No longer employed'),
    ('o', 'Other'),
)


class Location(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField(blank=True)
    latitude = models.CharField(max_length=16, blank=True)
    longitude = models.CharField(max_length=16, blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=128)

    @property
    def head(self):
        try:
            return Member.objects.get(department=self, is_department_head=True)
        except Member.DoesNotExist:
            pass

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class MemberManager(models.Manager):
    def employed(self):
        return Member.objects.filter(is_employed=True)


class Member(models.Model):

    objects = MemberManager()

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    title = models.CharField(max_length=128, blank=True)
    department = models.ForeignKey(Department, related_name='members', blank=True, null=True)
    is_department_head = models.BooleanField(default=False)

    is_employed = models.BooleanField(default=True)
    employment_status = models.CharField(max_length=4, choices=EMPLOYMENT_STATUSES)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    primary_location = models.ForeignKey(Location, related_name="members", blank=True, null=True)

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='staff/avatars', blank=True, null=True)
    alternate_avatar = models.ImageField(upload_to='staff/avatars-alt', blank=True, null=True)

    twitter = models.CharField(max_length=32, blank=True,
                               help_text="screenname only, no @")
    github = models.CharField(max_length=32, blank=True)

    office_phone = models.CharField(max_length=32, blank=True)
    cell_phone = models.CharField(max_length=32, blank=True)
    home_phone = models.CharField(max_length=32, blank=True)
    home_address = models.TextField(blank=True)

    emergency_name = models.CharField(max_length=128, blank=True)
    emergency_phone = models.CharField(max_length=32, blank=True)
    emergency_address = models.TextField(blank=True)

    slug = models.SlugField(unique=True, blank=True)
    guid = models.CharField(max_length=32, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return self.full_name()

    def save(self, **kwargs):

        # update is_employed
        self.is_employed = self.employment_status in ('ft', 'pt', 'i', 'f')

        # make sure there is only one department head
        if self.is_department_head:

            if self.employment_status != 'ft':
                raise ValueError('Only full time members can be a department head')

            qs = Member.objects.filter(department=self.department)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            qs.update(is_department_head=False)

        # make a slug if not created
        if not self.slug:
            self.slug = self.default_username()

        # ensure a guid is assigned
        if not self.guid:
            self.guid = uuid.uuid4().hex

        if self.twitter and self.twitter.startswith('@'):
            self.twitter = self.twitter[1:]

        super(Member, self).save(**kwargs)

    def default_username(self):
        return u"%s%s" % (self.first_name[0].lower(), self.last_name.replace('-', '').lower())

    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)
