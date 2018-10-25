
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='patients'
urlpatterns = [
    url(r'^$', views.index,name='home'),
    url(r'^pat_home/$', views.pat_home,name='pat_home'),
    url(r'^pat_logout/$', views.pat_logout,name='pat_logout'), 
    url(r'^doc/$', views.doc,name='doc'),
    url(r'^appointment/$', views.appointment,name='appointment'),
    url(r'^labrep/$', views.labrep,name='labrep'),
    url(r'^prescribe/$', views.prescribe,name='prescribe'),

	]

