from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.all_shops, name='shops'),
    path('shops/add-shop', views.add_shop, name='add-shop')
]