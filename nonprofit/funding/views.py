from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_tablib import ModelDataset
from nonprofit.funding.models import Contribution, Grant

MIMETYPES = {
    'csv': 'text/csv',
    'xls': 'application/vnd.ms-excel',
}

# tablib stuff


class ContributionDataset(ModelDataset):
    class Meta:
        queryset = Contribution.objects.all()


def dyn_amount(row):
    print row
    if row[5] == 'True':
        return '0.00'
    return row[3]

# the views


def funding(request):
    data = {
        'contributions': Contribution.objects.filter(is_inkind=False),
        'inkind': Contribution.objects.filter(is_inkind=True),
        'grants': Grant.objects.filter(is_minigrant=False),
        'minigrants': Grant.objects.filter(is_minigrant=True),
    }
    return render_to_response('about/funding.html', data, context_instance=RequestContext(request))


def funding_download(request, ext):

    ext = ext.lower()
    if ext not in MIMETYPES:
        raise Http404()

    data = ContributionDataset()
    data.headers = None
    data.append(col=[dyn_amount])
    data.headers = ['ID', 'Year', 'Contributor', 'Original Amount', 'Note', 'Is In-kind Contribution', 'Amount']
    del data['ID']                  # remove data column
    del data['Original Amount']     # remove original amount column

    return HttpResponse(getattr(data, ext), mimetype=MIMETYPES[ext])


def grants(request):
    data = {
        'grants': Grant.objects.filter(is_minigrant=False),
        'minigrants': Grant.objects.filter(is_minigrant=True),
    }
    return render_to_response('about/grants.html', data, context_instance=RequestContext(request))
