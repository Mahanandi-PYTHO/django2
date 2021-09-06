from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app1 import views

urlpatterns = [
    path('jbportal/',views.job_view,name= 'jbportal'),
    path('python/',views.python_view,name='python'),
    path('java/',views.java_view,name='java'),
    path('php/',views.php_view,name='php'),
    path('emp/',views.emp_view,name='emp'),


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)