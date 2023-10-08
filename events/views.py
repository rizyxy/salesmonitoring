from django.template import loader
from django.http import HttpResponse

def all_events(request):
    template = loader.get_template('all_events.html')
    return HttpResponse(template.render(None, request))
def add_events(request):
    template = loader.get_template('add_events.html')
    return HttpResponse(template.render(None, request))