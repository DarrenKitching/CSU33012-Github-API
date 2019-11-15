from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import plots

def getBar(request):
    context = {}
    context['myplots'] = plots.getBarChartData(request)
    return render(request, 'plotbar.html', context)

def getPie(request):
    context = {}
    context['myplots'] = plots.getPieChartData(request)
    return render(request, 'plotpie.html',context)

def getScatter(request):
    context = {}
    context['myplots'] = plots.getScatterPlotData(request)
    return render(request, 'plotscatter.html',context)

def index(request):
    template = loader.get_template('login.html')
    return render(request, 'login.html')

def submit(request):
    name = str(request.POST.get('uname'))
    password = str(request.POST.get('psw'))
    request.session['name'] = name 
    request.session['password'] = password 
    if plots.checkBadCredentials(name, password):
        return HttpResponseRedirect('badcredentials')
    else:    
        return HttpResponseRedirect('bar')

def badcredentials(request):
    template = loader.get_template('badcredentials.html')
    return HttpResponse(template.render())