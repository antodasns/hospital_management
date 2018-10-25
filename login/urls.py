
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='login'
urlpatterns = [
    url(r'^$', views.loginhome,name='loginhome'),
    url(r'^login/$', views.login,name='login'),
    url(r'^formdoc/$', views.formdoc,name='formdoc'),
    url(r'^formpat/$',views.formpat,name='formpat'),
    url(r'^formlab/$',views.formlab,name='formlab'),
    url(r'^view_doc/$',views.view_doc,name='view_doc'),
    url(r'^view_pat/$',views.view_pat,name='view_pat'),
    url(r'^view_lab/$',views.view_lab,name='view_lab'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^editdoc/(?P<id>\d+)$',views.editdoc,name='editdoc'),
    url(r'^updoc/(?P<id>\d+)$',views.updoc,name='updoc'),
    url(r'^deldoc/(?P<id>\d+)$',views.deldoc,name='deldoc'),
    url(r'^edit_lab/(?P<id>\d+)$',views.edit_lab,name='edit_lab'),
    url(r'^up_lab/(?P<id>\d+)$',views.up_lab,name='up_lab'),
    url(r'^del_lab/(?P<id>\d+)$',views.del_lab,name='del_lab'),
    url(r'^edit_pat/(?P<id>\d+)$',views.edit_pat,name='edit_pat'),
    url(r'^up_pat/(?P<id>\d+)$',views.up_pat,name='up_pat'),
    url(r'^del_pat/(?P<id>\d+)$',views.del_pat,name='del_pat'),
	]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

