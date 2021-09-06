import django
from Tools.scripts.make_ctype import method
from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.mail import send_mail

from app1.forms import Employee_form
from app1.models import Customer, Employee
from cbapp.forms import companiesModelform
from cbapp.models import companies


class cbsampleview(View):
    def get(self, request):
        print(dir(django.views))
        # View logic will place here
        return HttpResponse('response')





class customer_createview(CreateView):
    model = Customer
    fields = '__all__'
    success_url = '/list'

class customer_listview(ListView):
    model = Customer

class  customerDetail(DetailView):
    model = Customer


class  customerupdate(UpdateView):
    model = Customer
    fields="__all__"
    success_url = '/list'


class customerdelete(DeleteView):
    model = Customer
    success_url = '/list'
    template_name = 'app1/confirm_delete.html'

class companies_createview(CreateView):
    model = companies
    fields = '__all__'
    success_url = '/list1'

class companies_listview(ListView):
    model=companies
    fields='__all__'

class companies_detailview(DetailView):
    model = companies
    template_name = 'app1/companies_details.html'


class companies_deleteview(DeleteView):
    model=companies
    template_name = 'app1/cmpconfirm_delete.html'
    success_url = '/list1'


class  companiesupdate(UpdateView):
    model = companies
    fields="__all__"
    success_url = '/list1'


def add_companies(request):
   # mve = Movies.objects.all()
    form = companiesModelform()
    if request.method == "POST":
        form = companiesModelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list1')
    return render(request, 'app1/add_companies.html',{'form':form})

def mail(request):
    send_mail("hello rakesh","how are you???","rakeshmuthineni97@gmail.com", ['nadakuditi.ganeshkumar@gmail.com'],fail_silently=False)
    return render(request,'app1/index.html')

def login_view(request):
        #csrfContext = RequestContext(request)
        #return redirect('list1')
        return redirect('list')

    #return render(request,'forms/login.html')




def sample(request):
    query = 'SELECT * FROM cbapp_companies WHERE cname = %s' % cname
    vw=companies.objects.raw(query)
    print(vw)

    return render(request,'forms/sample.html')

def mail(request):
    subject = "Greetings"
    msg     = "Congratulations for your success"
    to      = "rakeshmuthineni9@gmail.com"
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)


