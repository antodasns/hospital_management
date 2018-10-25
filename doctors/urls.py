
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='doctors'
urlpatterns = [
    url(r'^$', views.index,name='home'),
    url(r'^doc_home/$', views.doc_home,name='doc_home'),
    url(r'^doc_logout/$', views.doc_logout,name='doc_logout'),
    url(r'^patappointment/$', views.patappointment,name='patappointment'),
    url(r'^patientview/$', views.patientview,name='patientview'),
    url(r'^consulting/(?P<id>\d+)$', views.consultings,name='consulting'),
    url(r'^submit_consult/(?P<id>\d+)$', views.submit_consult,name='submit_consult'),
	]

