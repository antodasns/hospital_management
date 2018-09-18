
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from login import views
app_name='login'
urlpatterns = [
    url(r'^$', views.loginhome,name='loginhome'),
    url(r'^login/$', views.login,name='login'),
    url(r'^formp/$', views.formp,name='formp'),

	]

