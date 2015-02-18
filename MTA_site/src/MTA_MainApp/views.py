
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def introduction(request):
  # template = loader.get_template('infotree_site/index.html')
  # return HttpResponse(template.render(context))
  return render(request, 'base.html',context_instance=RequestContext(request))
