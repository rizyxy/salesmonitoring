from django.db import models

class OnlineShop(models.Model):
    olshop_name = models.CharField(max_length=255)
    olshop_location = models.CharField(max_length=255)

class Product(models.Model):
    product_url = models.TextField()
    product_name = models.CharField(max_length=255)
    online_shop = models.ForeignKey(OnlineShop, on_delete=models.CASCADE)

class ProductHistory(models.Model):
    date_time = models.DateTimeField()
    sales = models.IntegerField()
    review_count = models.IntegerField()
    rating = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
