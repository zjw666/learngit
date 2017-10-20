from django.conf.urls import url
from . import views

app_name='web201'
urlpatterns=[
	url(r'^$',views.home,name="home"),
	url(r'^news/$',views.index,name="index"),
	url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
]

