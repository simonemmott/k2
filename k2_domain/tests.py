from django.test import TestCase
from jinja2 import Environment
from k2.jinja2 import environment
from jinja2 import PackageLoader
import json

jinja2_env = environment(loader=PackageLoader('k2_domain', 'jinja2'))

# Create your tests here.
class Jinja2Tests(TestCase):
    
    def test_template_from_string(self):
        template = jinja2_env.from_string('Hello {{target}}!')
        output = template.render(target='World')
        self.assertEqual('Hello World!', output)
        
    def test_list_from_string(self):
        template = jinja2_env.from_string('[{% for model in domain.models %}{{model.name}}.py,{% endfor %}]')
        class Domain(object):
            pass
        class Model(object):
            pass
        domain = Domain()
        domain.name = 'NAME'
        model1 = Model()
        model1.name = 'MODEL_1'
        model2 = Model()
        model2.name = 'MODEL_2'
        domain.models = [model1, model2]
        
        lst = template.render(domain=domain)[1:-2].split(',')
        self.assertEquals('MODEL_1.py', lst[0])
        self.assertEquals('MODEL_2.py', lst[1])
        