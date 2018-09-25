
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from login import views
app_name='login'
urlpatterns = [
    url(r'^$', views.loginhome,name='loginhome'),
    url(r'^login/$', views.login,name='login'),
    url(r'^formdoc/$', views.formdoc,name='formdoc'),
    url(r'^formpat/$',views.formpat,name='formpat'),
    url(r'^view_doc/$',views.view_doc,name='view_doc'),
    url(r'^view_pat/$',views.view_pat,name='view_pat'),
    url(r'^view_lab/$',views.view_lab,name='view_lab'),
	]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

