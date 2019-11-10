from django.urls import path
from .views import MyBar, MyPie


urlpatterns = [
	path('bar', MyBar.as_view(),name='myplots'),
	path('pie', MyPie.as_view(),name='myplots'),
]