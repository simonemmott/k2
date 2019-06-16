from django.urls import path
from .views import DomainSourceView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
        path('src/<int:domain_id>/', DomainSourceView.as_view()),

]