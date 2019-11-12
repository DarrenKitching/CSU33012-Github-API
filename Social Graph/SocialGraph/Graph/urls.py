from django.urls import path
from .views import MyBar, MyPie, MyScatter, index, submit, badcredentials


urlpatterns = [
	path('', index, name='index'),
	path('badcredentials', badcredentials, name='badcredentials'),
	path('submit', submit, name='submit'),
	path('bar', MyBar.as_view(),name='myplots'),
	path('pie', MyPie.as_view(),name='myplots'),
	path('scatter', MyScatter.as_view(),name='myplots')
]