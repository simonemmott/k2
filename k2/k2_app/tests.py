from django.test import TestCase
from . import templates

def index_error():
    templates.index('k2_app', 'jinja2/k2_app/__init__.py')
    
class SourceTests(TestCase):
    
    def test_index(self):
        index = templates.index('k2_app', 'k2_app/k2')
        self.assertEqual('k2_app/k2/__init__.py', index['__init__.py'])
        self.assertEqual('k2_app/k2/jinja2.py', index['jinja2.py'])
        self.assertEqual('k2_app/k2/settings.py', index['settings.py'])
        self.assertEqual('k2_app/k2/urls.py', index['urls.py'])
        self.assertEqual('k2_app/k2/wsgi.py', index['wsgi.py'])
            
        self.assertRaises(ValueError, index_error)
        