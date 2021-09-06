"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from app1 import views
from cbapp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('menubar/', views.menu_bar, name='menubar'),
    path('auto_slide/', views.auto_slide, name='auto_slide'),
    path('app1', include('app1.urls')),
    path('djangofrm',views.djangoform_view,name='djangofrm'),
    path('modelform/', views.modelform_view, name='modelform'),
    path('htmlform/', views.htmlform_view, name='htmlform'),
    path('movies/', views.Movies_view,name='movies'),
    path('employee1/', views.emp_view1, name='employee'),
    path('edit_emp/<int:id>', views.edit_emp_view, name='edit_emp'),
    path('del_emp/<int:id>', views.dele_emp_view, name='del_emp'),
    path('del_conf/<int:id>', views.dele_conf, name='delemp_conf'),
    path('edit_mve/<int:id>', views.movie_editview, name='edit_mve'),
    path('editmodel_mve/<int:id>', views.moviemodel_editview, name='editmodel_mve'),
    path('mve_del/<int:did>', views.mov_delview, name='mve_del'),
    path('add_mve/', views.add_mvemodel_view, name='add_mve'),
    path('cbsample/', v1.cbsampleview.as_view(), name='cbsample'),
    path('create/', v1.customer_createview.as_view(), name='create'),
    path('list/', v1.customer_listview.as_view(), name='list'),
    path('detail/<int:pk>', v1.customerDetail.as_view(), name = 'detail'),
    path('update/<int:pk>', v1.customerupdate.as_view(), name = 'update'),
    path('delete/<int:pk>', v1.customerdelete.as_view(), name = 'delete'),
    path('cbapp/', include('cbapp.urls')),
    path('cmpcreate/', v1.companies_createview.as_view(), name = 'cmpcreate'),
    path('list1/', v1.companies_listview.as_view(), name = 'list1'),
    path('detail1/<int:pk>', v1.companies_detailview.as_view(), name = 'detail1'),
    path('delete1/<int:pk>', v1.companies_deleteview.as_view(), name = 'delete1'),
    path('update1/<int:pk>', v1.companiesupdate.as_view(), name = 'update1'),
    path('mail/', v1.mail, name ='mail'),
    path('add_cmp/', v1.add_companies, name ='add_cmp'),
    path('login/', v1.login_view, name ='login'),



]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)