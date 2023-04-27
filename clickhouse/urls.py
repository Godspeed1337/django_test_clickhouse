from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('avg', views.average, name='avg'),
    path('graph', views.graph, name='graph'),
]