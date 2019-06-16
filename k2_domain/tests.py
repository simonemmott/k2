from django.test import TestCase
from jinja2 import Environment

# Create your tests here.
class Jinja2Tests(TestCase):
    
    def test_template_from_string(self):
        template = Environment.from_string('Hello {{target}}!')
        output = template.render(target='World')
        self.assertEqual('Hello World!', output)
        
#    def test_list_from_string(self):
#        template = Environment.from_string('[{% for model in domin.models %}{{model.name}}.py,{% endfor %}]')
#        model1 = {}
#        domain = {}
#        setattr(model1, 'name', 'model1')
#        model2 = {}
#        setattr(model2, 'name', 'model2')
#        setattr(domain, 'models', [model1, model2])
#        output = template.render(domain=domain)
        print(output)