
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='laboratory'
urlpatterns = [
    url(r'^$', views.index,name='laboratory'),
    url(r'^pat/$', views.pat,name='pat'),
    url(r'^lab_home/$', views.lab_home,name='lab_home'),
    url(r'^doc/$', views.doc,name='doc'),
    url(r'^result/$', views.result,name='result'),
    url(r'^lab_logout/$', views.lab_logout,name='lab_logout'),
    url(r'^submit/$', views.submit_result,name='submit_result'),
	]

