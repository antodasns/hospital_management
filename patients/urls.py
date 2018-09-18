
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='patients'
urlpatterns = [
    url(r'^$', views.index,name='home'),
    url(r'^login/$', views.login,name='login'),
    url(r'^registration/$', views.login,name='registration'),
    url(r'^ser/$', views.ser,name='ser'),  
    url(r'^doc/$', views.doc,name='doc'),
    url(r'^appointment/$', views.appointment,name='appointment'),
    url(r'^labrep/$', views.labrep,name='labrep'),
	]

