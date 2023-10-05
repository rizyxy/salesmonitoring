from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.all_events, name='all-events')
]