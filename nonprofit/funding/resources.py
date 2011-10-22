from tastypie.resources import ModelResource
from nonprofit.funding.models import Contribution, Grant

class ContributionResource(ModelResource):
    class Meta:
        queryset = Contribution.objects.all()
        resource_name = 'contribution'

class GrantResource(ModelResource):
    class Meta:
        queryset = Grant.objects.all()
        resource_name = 'grant'