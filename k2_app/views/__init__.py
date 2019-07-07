from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView, View
from rest_framework.response import Response
from rest_framework.views import APIView
from k2_app.models.application import Application
from k2.errors import K2Error, K2SourceError
from k2_core import templates
from jinja2.exceptions import TemplateSyntaxError
import logging
import traceback
import json
from k2_core import jinja2

logger = logging.getLogger(__name__)



def index(request):
    return HttpResponse("Hello, world. You're at the k2_app index.")

def python_response(body):
    return HttpResponse(body, content_type='text/python')

def directory_response(index):
    return JsonResponse(
        index, 
        content_type='application/k2-directory', 
        json_dumps_params={'indent': 4}
    )
    
def error_response(err, status=500):
    logger.exception(str(err))
    resp = {'error': str(err), 'trace': traceback.format_exc()}
    return JsonResponse(
        {'error': str(err), 'trace': traceback.format_exc()}, 
        json_dumps_params={'indent': 4}, 
        status=status
    )
    
class ApplicationView(APIView):
    
    def get(self, request, id):
        logger.debug('ApplicationView.GET({id})'.format(id=id))
        try:
            if id.isdigit():
                app = Application.objects.get(id=id)
            else:
                app = Application.objects.get(name=id)
        except Application.DoesNotExist:
            return HttpResponse(status=404)
        
        return JsonResponse(ApplicationSerializer(app).data)

class ApplicationSourceView(APIView):
    
    def get(self, request, app_id):
        logger.debug('ApplicationSourceView.GET({id})'.format(id=app_id))
        path = request.GET.get('path', None)     
        app = Application.objects.get(id=app_id)
        try:
            if path:
                try:
                    return directory_response(templates.index(jinja2.env, path))
                except:
                    template = jinja2.env.get_template(path)
                    return python_response(template.render(app=app))                                        
            else:
                return directory_response(templates.application_index(app))
        except Exception as err:
            return error_response(err)

        
        
        