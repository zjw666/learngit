from django.conf.urls import url
from . import views

app_name='web201'
urlpatterns=[
	url(r'^$',views.home,name="home"),
	url(r'^introduction/$',views.introduction,name="introduction"),
	url(r'^teachers-(?P<name>li|wang)/$',views.teachers,name="teachers"),
	url(r'^students/$',views.students,name="students"),
	url(r'^news/(?P<type>life|academic|happy)/$',views.news,name="news"),
	url(r'^news/(?P<type>life|academic|happy)/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
	url(r'^search/$',views.search,name='search'),
]

