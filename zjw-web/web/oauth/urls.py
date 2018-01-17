from django.conf.urls import url
from . import views

app_name='oauth'
urlpatterns=[
	url(r'github_login',views.git_login,name='github_login'),
	url(r'github_check',views.git_check,name='github_check'),
	url(r'qq_login',views.qq_login,name='qq_login'),
	url(r'qq_check',views.qq_check,name='qq_check'),
	url(r'weibo_login',views.weibo_login,name='weibo_login'),
	url(r'weibo_check',views.weibo_check,name='weibo_check'),
	url(r'bind_email',views.bind_email,name='bind_email'),
]

