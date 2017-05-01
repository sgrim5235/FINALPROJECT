from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HeyView(TemplateView):
    template_name = 'OurPage.html'