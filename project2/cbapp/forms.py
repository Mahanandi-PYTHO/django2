from django import forms

from app1.models import Customer, Employee
from cbapp.models import companies



class CustomerModelform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class companiesModelform(forms.ModelForm):
    class Meta:
        model = companies
        fields = '__all__'

class EmployeeModelform(forms.ModelForm):
        class Meta:
            model = Employee
            fields = '__all__'
