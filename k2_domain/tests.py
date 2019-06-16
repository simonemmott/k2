from django.test import TestCase
from jinja2 import Environment
from k2.jinja2 import environment
from jinja2 import PackageLoader
import json
from k2_app import templates
from posix import lstat

jinja2_env = environment(loader=PackageLoader('k2_domain', 'jinja2'))

def test_domain():
        class Object(object):
            pass
        class List(object):
            def __init__(self, lst):
                self.lst = lst
            def all(self):
                return self.lst
                
        domain = Object()
        domain.name = 'DOMAIN_NAME'
        model1 = Object()
        model1.id = 1
        model1.name = 'MODEL_1'
        model2 = Object()
        model2.id = 2
        model2.name = 'MODEL_2'
        domain.models = List([model1, model2])
        
        return domain
    
# Create your tests here.
class Jinja2Tests(TestCase):
    
    def test_template_from_string(self):
        template = jinja2_env.from_string('Hello {{target}}!')
        output = template.render(target='World')
        self.assertEqual('Hello World!', output)
        
    def test_list_from_string(self):
        template = jinja2_env.from_string('[{% for model in domain.models.all() %}{{model.name}}.py,{% endfor %}]')
        
        lst = template.render(domain=test_domain())[1:-2].split(',')
        self.assertEquals('MODEL_1.py', lst[0])
        self.assertEquals('MODEL_2.py', lst[1])
        
class IndexTests(TestCase):
    
    def test_indexes(self):

        index = templates.index('k2_domain', 'k2_domain', domain=test_domain())
        self.assertEquals(1, len(index))
        self.assertTrue('DOMAIN_NAME' in index.keys())
        self.assertEquals('k2_domain/domain.name', index.get('DOMAIN_NAME'))
        
        index = templates.index('k2_domain', 'k2_domain/domain.name/models', domain=test_domain())
        self.assertEquals(3, len(index))
        self.assertTrue('__init__.py' in index.keys())
        self.assertEquals('k2_domain/domain.name/models/__init__.py', index.get('__init__.py'))
        self.assertTrue('MODEL_1.py' in index.keys())
        self.assertEquals('k2_domain/domain.name/models/model.py&model=1', index.get('MODEL_1.py'))
        self.assertTrue('MODEL_2.py' in index.keys())
        self.assertEquals('k2_domain/domain.name/models/model.py&model=2', index.get('MODEL_2.py'))

        