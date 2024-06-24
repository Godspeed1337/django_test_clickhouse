from django.urls import path

from . import views

urlpatterns = [
    path('add_2', views.add, name='add'),
    path('avg', views.average, name='avg'),
    path('graph', views.graph, name='graph'),
]