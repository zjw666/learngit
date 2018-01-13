from django.conf.urls import url
from . import views

app_name='oauth'
urlpatterns=[
	url(r'git_login',views.git_login,name='git_login'),
	url(r'git_check',views.git_check,name='git_check'),
	url(r'bind_email',views.bind_email,name='bind_email'),
]

