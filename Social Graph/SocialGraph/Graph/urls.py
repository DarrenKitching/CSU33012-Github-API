from django.urls import path
from .views import getBar, getPie, getScatter, index, submit, badcredentials


urlpatterns = [
	path('', index, name='index'),
	path('badcredentials', badcredentials, name='badcredentials'),
	path('submit', submit, name='submit'),
	path('bar', getBar,name='myplots'),
	path('pie', getPie,name='myplots'),
	path('scatter', getScatter,name='myplots')
]