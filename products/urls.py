from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all-products'),
    path('/products/add-product', views.add_product, name='add-product')
]