import csv

from django.contrib.sessions.backends import file
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mail(request):
    send_mail("hello rakesh","how are you???","mahanandi419@gmail.com", ['rakeshmuthineni9@gmail.com'],fail_silently=False)
    return render(request,'index.html')

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', '', 'arjun'])
    writer.writerow(['Date', 's.no', '', 'Work'])
    writer.writerow(['24.8.21','1','','Working on it....'])
    return response


def my_view(request):
    context = {
        "author": "gaurav singhal",
    }
    return render(request, "modify_name.html", context)