from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from . import plots

name = None
password = None

class MyBar(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyBar, self).get_context_data(**kwargs)
        context['myplots'] = plots.getBarChartData(name, password)
        return context

class MyPie(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(MyPie, self).get_context_data(**kwargs)
        context['myplots'] = plots.getPieChartData(name, password)
        return context

def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def submit(request):
    global name
    global password
    name = str(request.POST.get('uname'))
    password = str(request.POST.get('psw'))
    return HttpResponseRedirect('bar')