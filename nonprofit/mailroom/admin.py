from django.contrib import admin
from nonprofit.mailroom.models import Slot

class SlotAdmin(admin.ModelAdmin):
    list_display = ('description','forward_to','enabled')

admin.site.register(Slot, SlotAdmin)