from django.views.generic import TemplateView
from . import plots

class MyBar(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyBar, self).get_context_data(**kwargs)
        name = 'DarrenKitching'
        password = ''
        context['myplots'] = plots.getBarChartData(name, password)
        return context

class MyPie(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyPie, self).get_context_data(**kwargs)
        name = 'DarrenKitching'
        password = ''
        context['myplots'] = plots.getPieChartData(name, password)
        return context