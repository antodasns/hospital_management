
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='laboratory'
urlpatterns = [
    url(r'^$', views.index,name='laboratory'),
    url(r'^pat/$', views.pat,name='pat'),
    url(r'^doc/$', views.doc,name='doc'),
    url(r'^test/$', views.test,name='test'),
	]

