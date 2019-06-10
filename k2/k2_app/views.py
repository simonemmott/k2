from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the k2_app index.")

class TestView(TemplateView):
    template_name = "app/test.html"
