from django.contrib.syndication.views import Feed
from nonprofit.helpwanted.models import JobListing


class OpenPositionsFeed(Feed):

    title = "Current Open Positions"
    description = "Current Open Positions"

    title_template = "helpwanted/feeds/title.html"
    description_template = "helpwanted/feeds/description.html"

    def link(self):
        from django.core.urlresolvers import reverse
        return reverse('job_list')

    def items(self):
        return JobListing.objects.open()

    def item_description(self, job_listing):
        return

    def item_author_name(self, job_listing):
        return job_listing.contact_name

    def item_pubdate(self, job_listing):
        return job_listing.date_published
