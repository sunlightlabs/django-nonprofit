from django.contrib import admin
from nonprofit.funding.models import Contribution,  Grant


class ContributionAdmin(admin.ModelAdmin):
    list_display = ('year', 'contributor', 'amount', 'is_inkind')
    list_filter = ('year', 'is_inkind')
    search_fields = ('contributor', 'note')
admin.site.register(Contribution,  ContributionAdmin)


class GrantAdmin(admin.ModelAdmin):
    list_display = ('year', 'recipient', 'amount', 'is_minigrant')
    list_filter = ('year', 'is_minigrant')
    search_fields = ('recipient', 'purpose')
admin.site.register(Grant,  GrantAdmin)
