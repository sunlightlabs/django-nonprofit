from tastypie.resources import ModelResource
from nonprofit.mailroom.models import Slot

class SlotResource(ModelResource):
    class Meta:
        queryset = Slot.objects.all()
        resource_name = 'slot'