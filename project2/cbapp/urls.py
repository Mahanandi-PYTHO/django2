from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cbapp import views as v1

urlpatterns = [
        path('cmpcreate/', v1.companies_createview.as_view(), name = 'cmpcreate'),
        path('list/', v1.companies_listview.as_view(), name = 'list'),
        path('sample/', v1.sample, name = 'sample'),
        path('mail',v1.mail,name='email')


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)