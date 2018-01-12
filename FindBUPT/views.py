__author__ = 'xiaoyue, Daivd Young'

from django.shortcuts import render,render_to_response,RequestContext

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render_to_response('index.html', context_instance=RequestContext(request))