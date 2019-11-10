from django.views.generic import TemplateView
from . import plots

class MyBar(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyBar, self).get_context_data(**kwargs)
        context['myplots'] = plots.getBarChartData('DarrenKitching')
        return context

class MyPie(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyPie, self).get_context_data(**kwargs)
        context['myplots'] = plots.getPieChartData('DarrenKitching')
        return context