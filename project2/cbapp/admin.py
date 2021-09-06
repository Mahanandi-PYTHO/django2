from django.contrib import admin

# Register your models here.

from cbapp.models import companies


class companiesAdmin(admin.ModelAdmin):
    list_display = ['cname','skills','roles','address','logo']
    list_display_links = ['cname']

admin.site.register(companies, companiesAdmin)