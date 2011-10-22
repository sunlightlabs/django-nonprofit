from tastypie.resources import ModelResource
from nonprofit.staff.models import Location, Department, Member

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'

class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'department'

class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'