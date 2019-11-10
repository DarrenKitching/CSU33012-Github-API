from django.urls import path
from .views import MyBar, MyPie, index, submit


urlpatterns = [
	path('', index, name='index'),
	path('submit', submit, name='index'),
	path('bar', MyBar.as_view(),name='myplots'),
	path('pie', MyPie.as_view(),name='myplots'),
]