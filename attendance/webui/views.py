from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class LamdingPage(TemplateView):
    template_name = "base.html"

def index(request):
    return HttpResponse("hello Woerld")