from django.conf.urls import url
from django.urls import path
from . import views
from .views import ApplicationSourceView

urlpatterns = [
    path('', views.index, name='index'),
    path('src/<int:app_id>/', ApplicationSourceView.as_view()),
]
