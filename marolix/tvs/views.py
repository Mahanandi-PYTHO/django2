from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):

    return HttpResponse('helloo')
def html(request):

    return render(request,'temp/sample.html')