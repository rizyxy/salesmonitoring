from django.http import HttpResponse
from django.template import loader
from master.models import Product

def all_products(request):
    products = Product.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'products': products
    }

    return HttpResponse(template.render(context, request))
