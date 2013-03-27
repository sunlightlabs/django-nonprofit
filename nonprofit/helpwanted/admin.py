from django.contrib import admin
from nonprofit.helpwanted.models import JobListing


class JobListingAdmin(admin.ModelAdmin):
    list_display = ('is_filled', 'position_type', 'position', 'organization',
                    'date_published', 'is_expired')
    list_display_links = ('position',)
    list_filter = ('position_type', 'is_filled')
    search_fields = ('position', 'position_description', 'organization', 'location')

admin.site.register(JobListing, JobListingAdmin)
