# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        return context
