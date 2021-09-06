"""django1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from dell import views as v1
from hp import views as v2
from db import views as m1
from poll import views as v5
from db import models as m


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', v1.time, name='greet'),
    path('msg/', v2.msg, name='msg'),
    path('time/', m1.index, name='time'),
    path('index', v5.index, name='index'),
]
