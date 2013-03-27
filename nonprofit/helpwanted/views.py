from django.views.generic import DetailView, ListView
from nonprofit.helpwanted.models import JobListing


class JobDetail(DetailView):

    context_object_name = 'id'
    queryset = JobListing.objects.all()

    def get_context_data(self, **kwargs):

        pk = self.kwargs['pk']
        other_jobs = JobListing.objects.open().exclude(pk=pk).order_by("?")[:5]

        context = super(JobDetail, self).get_context_data(**kwargs)
        context['other_jobs'] = other_jobs
        return context


class JobList(ListView):

    allow_empty = True
    paginate_by = 10
    queryset = JobListing.objects.open()
    template_object_name = "job"
