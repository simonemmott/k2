from django.conf.urls import url
from django.urls import path
from . import views
from .views import ApplicationView, ApplicationSourceView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/application/<str:id>/', ApplicationView.as_view()),
    path('src/<int:app_id>/', ApplicationSourceView.as_view()),
]
