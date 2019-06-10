from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from k2.jinja2 import environment
from k2.errors import K2Error, K2SourceError
from jinja2 import PackageLoader

def index(request):
    return HttpResponse("Hello, world. You're at the k2_app index.")

class TestView(TemplateView):
    template_name = "app/test.html"

jinja2_env = environment(loader=PackageLoader('k2_app', 'jinja2'))

class ApplicationSourceView(View):
    
    def get(self, request, app_id):
        name = request.GET.get('template_name', None)     
        app = Application.objects.get(id=app_id)
        if name:
            template = jinja2_env.get_template(name)
            return HttpResponse(template.render(app=app))
        else:
            raise K2SourceError('No template given')

        
        
        