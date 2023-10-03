from django.http import HttpResponse
from django.template import loader

# Create your views here.
def graph(request):
    template = loader.get_template('graph.html')
    return HttpResponse(template.render(None, request))