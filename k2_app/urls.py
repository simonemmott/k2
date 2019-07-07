from django.conf.urls import url
from django.urls import path
from . import views
from .views import ApplicationView, ApplicationSourceView
from .views.package import PackageList
from .views.package import PackageDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('api/application/<str:id>/', ApplicationView.as_view()),
    path('src/<int:app_id>/', ApplicationSourceView.as_view()),
    path('api/packages/', PackageList.as_view()),
    path('api/package/<str:name>/', PackageList.as_view()),
]
