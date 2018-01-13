from django.conf.urls import url
from . import views

app_name='oauth'
urlpatterns=[
	url(r'github_login',views.git_login,name='github_login'),
	url(r'github_check',views.git_check,name='github_check'),
	url(r'bind_email',views.bind_email,name='bind_email'),
]

