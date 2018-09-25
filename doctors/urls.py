
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='doctors'
urlpatterns = [
    url(r'^$', views.index,name='home'),
    url(r'^patappointment/$', views.patappointment,name='patappointment'),
    url(r'^patientname/$', views.patientname,name='patientname'),
    url(r'^consulting/$', views.consulting,name='consulting'),
	]

