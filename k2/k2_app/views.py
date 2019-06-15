from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView, View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from k2.jinja2 import environment
from k2.errors import K2Error, K2SourceError
from jinja2 import PackageLoader
from . import templates
from jinja2.exceptions import TemplateSyntaxError
import logging
import traceback
import json

logger = logging.getLogger(__name__)



def index(request):
    return HttpResponse("Hello, world. You're at the k2_app index.")

jinja2_env = environment(loader=PackageLoader('k2_app', 'jinja2'))

def python_response(body):
    return HttpResponse(body, content_type='text/python')

def directory_response(index):
    return JsonResponse(
        index, 
        content_type='application/k2-directory', 
        json_dumps_params={'indent': 4}
    )
    
def error_response(err, status=500):
    logger.exception(err.message)
    resp = {'error': err.message, 'trace': traceback.format_exc()}
    return JsonResponse(
        {'error': err.message, 'trace': traceback.format_exc()}, 
        json_dumps_params={'indent': 4}, 
        status=status
    )

class ApplicationSourceView(APIView):
    
    def get(self, request, app_id):
        path = request.GET.get('path', None)     
        app = Application.objects.get(id=app_id)
        try:
            if path:
                try:
                    return directory_response(templates.index('k2_app', path))
                except:
                    template = jinja2_env.get_template(path)
                    return python_response(template.render(app=app))                                        
            else:
                raise K2SourceError('No template given')
        except Exception as err:
            return error_response(err)

        
        
        