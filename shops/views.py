from django.http import HttpResponse
from django.template import loader

def all_shops(request):
    template = loader.get_template('all_shops.html')
    return HttpResponse(template.render(None, request))