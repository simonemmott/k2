from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.template import Context
from . import views
from .views import TestView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^test/$', TestView.as_view(), {'test': 'XXX'}),
    url(r'^test2/$', TemplateView.as_view(template_name='app/test.html'), {'test': 'YYY'}),
]
