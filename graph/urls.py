from django.urls import path
from . import views

urlpatterns = [
    path('graphs/', views.graph, name='all-graphs'),
]