from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_index(request):
    return render(request, 'func_template.html')

class class_index(TemplateView):
    template_name = 'class_template.html'