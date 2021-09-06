from django.contrib import admin
from app1.models import Employee
from app1.models import Student
from app1.models import Customer
from app1.models import Books
from app1.models import Movies


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'email', 'esalary', 'edate', 'status']
    list_display_links = ['ename']
    search_fields = ['id']
    list_per_page = 2


admin.site.register(Employee,EmployeeAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sname', 'branch', 'roll_no', 'college', 'fees', 'status']
    search_fields = ['ename']


admin.site.register(Student, StudentAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'email', 'phone', 'village', 'order', 'status', ]
    search_fields = ['sname']
    list_display_links = ['phone']


admin.site.register(Customer, CustomerAdmin)


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'sub', 'author', 'email', 'phone', 'price', 'status', ]
    search_fields = ['date']
    list_display_links = ['phone']

admin.site.register(Books, BooksAdmin)


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'mtitle', 'hero', 'heroin', 'desc', 'release_date', 'status']
    search_fields = ['mtitle']
    list_display_links = ['mtitle']


admin.site.register(Movies,MoviesAdmin)
