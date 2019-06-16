from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView, View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Domain, Model
from k2.jinja2 import environment
from k2.errors import K2Error, K2SourceError
from jinja2 import PackageLoader
from k2_app import templates
from jinja2.exceptions import TemplateSyntaxError
import logging
import traceback
import json

logger = logging.getLogger(__name__)



def index(request):
    return HttpResponse("Hello, world. You're at the k2_domain index.")

jinja2_env = environment(loader=PackageLoader('k2_domain', 'jinja2'))

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

class DomainSourceView(APIView):
    
    def get(self, request, domain_id):
        logger.debug('DomainSourceView.get({id})'.format(id=domain_id))
        path = request.GET.get('path', None)
        logger.debug('GET path: {path}'.format(path=path))
        domain = Domain.objects.get(id=domain_id)
        kw = {
            'domain': domain
        }
        for parm in request.GET.keys():
            if parm == 'model':
                id = request.GET.get('model')
                model = Model.objects.get(id=id)
                kw['model'] = model
                logger.debug('GET model: {name}'.format(name=model.name))
                
        try:
            if path:
                try:
                    return directory_response(templates.index('k2_domain', path, **kw))
                except:
                    template = jinja2_env.get_template(path)
                    return python_response(template.render(**kw))                                        
            else:
                raise K2SourceError('No template given')
        except Exception as err:
            return error_response(err)

        
        
