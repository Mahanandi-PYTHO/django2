from django.shortcuts import render, redirect

# Create your views here.
from numpy.lib.function_base import delete

from app1.forms import MoviesModelform, Movies_form, Employee_form
from app1.models import Employee
from app1.models import Movies


def home_view(request):
    return render(request,'app1/home.html')

def menu_bar(request):
    return render(request,'menubar.html')
def auto_slide(request):
    return render(request,'app1/auto_slide.html')

def job_view(request):

    return render(request,'jobs/home.html')

def python_view(request):
    image1="wipro.jpg"
    cname1="Wipro"
    posted_date="post_Date9/8/2021."
    cdesc1="Required skill :"
    image2 = "logo1.jpg"
    cname2 = "Marolix Tech Solutions"
    posted_date ="post_Date  9/8/2021."
    cdesc2 = "Required skills :"
    image3 = "tcs.jpg"
    cname3 = "Tata consultancy service."
    posted_date ="posted date : 9/8/2021."
    cdesc3 = "Required skills :"
    context = {'image1':image1,'cname1':cname1,'posted_date':posted_date,'cdesc1':cdesc1,'image2':image2,'cname2':cname2,'posted_date':posted_date,'cdesc2':cdesc2,'image3':image3,'cname3':cname3,'posted_date':posted_date,'cdesc3':cdesc3}
    return render(request,'jobs/python.html',context)

def java_view(request):
    image1 = "accen.jpg"
    cname1 = "Accenture IT"
    posted_date = "post_Date9/8/2021."
    cdesc1 = "Required skill :"
    image2 = "logo1.jpg"
    cname2 = "Marolix Tech Solutions"
    posted_date = "post_Date  9/8/2021."
    cdesc2 = "Required skills :"
    image3 = "cognizant1.jpg"
    cname3 = "Cognizant IT"
    posted_date = "posted date : 9/8/2021."
    cdesc3 = "Required skills :"
    context = {'image1': image1, 'cname1': cname1, 'posted_date': posted_date, 'cdesc1': cdesc1, 'image2': image2,
               'cname2': cname2, 'posted_date': posted_date, 'cdesc2': cdesc2, 'image3': image3, 'cname3': cname3,
               'posted_date': posted_date, 'cdesc3': cdesc3}
    return render(request, 'jobs/java.html', context)


def php_view(request):
    image1 = "amazon.jpg"
    cname1 = "Amazon IT"
    posted_date = "post_Date9/8/2021."
    cdesc1 = "Required skill :"
    image2 = "logo1.jpg"
    cname2 = "Marolix Tech Solutions"
    posted_date = "post_Date  9/8/2021."
    cdesc2 = "Required skills :"
    image3 = "google.jpg"
    cname3 = "Google Ltd"
    posted_date = "posted date : 9/8/2021."
    cdesc3 = "Required skills :"
    context = {'image1': image1, 'cname1': cname1, 'posted_date': posted_date, 'cdesc1': cdesc1, 'image2': image2,
               'cname2': cname2, 'posted_date': posted_date, 'cdesc2': cdesc2, 'image3': image3, 'cname3': cname3,
               'posted_date': posted_date, 'cdesc3': cdesc3}
    return render(request,'jobs/php.html', context)

def emp_view(request):
    emp=Employee.objects.all()
    print(emp)
    return render(request,'app1/emp.html',{'emp':emp})
def Movies_view(request):
    mve = Movies.objects.filter(status=True)
    return render(request,'app1/Movies.html',{'mve':mve})

def htmlform_view(request):
    if request.method=="POST":
        mvs = Movies(mtitle=request.POST['mname'],hero=request.POST['hero'],heroin=request.POST['heroin'],desc=request.POST['desc'],release_date=request.POST['date'],mimage=request.FILES['image'])
        mvs.save()
        return redirect('movies')
    return render(request,'forms/htmlform.html')

def djangoform_view(request):
    form=Movies_form()
    if request.method == "POST":
        mvs = Movies(mtitle=request.POST['mtitle'],hero=request.POST['hero'],heroin=request.POST['heroin'],desc=request.POST['desc'],release_date=request.POST['release_date'], mimage=request.FILES['mimage'])
        mvs.save()
        return redirect('movies')
    return render(request,'forms/djangoform.html',{'form':form})


def modelform_view(request):
    form=MoviesModelform()
    if request.method == "POST":
        form = Movies_form(request.POST,request.FILES)
        if form.is_valid():
         return redirect('movies')
    return render(request,'forms/modelform.html', {'form': form})

def emp_view1(request):
    emp=Employee.objects.filter(status=True)
    print(emp)
    return render(request,'app1/employee.html',{'emp':emp})

def edit_emp_view(request,id):
    emp=Employee.objects.get(id=id,status=True)
    form = Movies_form(request.POST, request.FILES)
    if request.method=="POST":
        ename=request.POST['ename']
        email = request.POST['email']
        salary = request.POST['esalary']
        res_up=Employee.objects.get(id=id)
        res_up.ename=ename
        res_up.email = email
        res_up.esalary = salary
        res_up.save()
        return redirect('employee')
    return render(request,'app1/edit_employee.html',{'emp':emp})

def dele_emp_view(request,id):
    return render(request,'app1/del_emp.html',{'eid':id})

def dele_conf(request,id):
    emp=Employee.objects.get(id=id,status=True)
    emp.delete()
    return redirect('employee')

def movie_editview(request,id):
    mve=Movies.objects.get(id=id)
    if request.method=="POST":
        mname=request.POST['mtitle']
        hero = request.POST['hero']
        heroin = request.POST['heroin']
        desc = request.POST['desc']
        release_date = request.POST['date']
        mimage = request.FILES['mimage']
        res_up =Movies.objects.get(id=id)
        res_up.mtitle=mname
        res_up.hero = hero
        res_up.heroin = heroin
        res_up.desc = desc
        res_up.release_date = release_date
        res_up.mimage = mimage
        res_up.save()
        return redirect('movies')
    return render(request,'app1/movie_edit.html',{'mve':mve})
def moviemodel_editview(request,id):
    mve = Movies.objects.get(id=id)
    form=MoviesModelform(instance=mve)
    if request.method=="POST":
        form = MoviesModelform(request.POST,request.FILES)
        if form.is_valid():
            form = MoviesModelform(request.POST,request.FILES ,instance=mve)
            form.save()
            return redirect('movies')
    return render(request, 'app1/moviemodel_edit.html', {'form': form})

def add_mvemodel_view(request):
   # mve = Movies.objects.all()
    form = MoviesModelform()
    if request.method == "POST":
        form = MoviesModelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request, 'app1/add_mve.html',{'form':form})


def mov_delview(request,did):
    print("dsfdsfds")
    mve=Movies.objects.get(id=did)
    mve.status=False
    mve.save()
    return redirect('movies')
