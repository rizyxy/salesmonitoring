from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.all_events, name='all-events'),
    path('/events/add-events', views.add_events, name='add-events')
]