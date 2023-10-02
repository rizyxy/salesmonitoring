from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.all_shops, name='shops')
]