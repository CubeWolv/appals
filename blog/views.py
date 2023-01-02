from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def privacypolicy(request):
  template = loader.get_template('./privacypolicy101/privacypolicy101.html')
  return HttpResponse(template.render())

  
def about(request):
    return render(request, './about/about.html')