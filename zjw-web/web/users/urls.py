from django.conf.urls import url
from . import views

app_name= 'users'
urlpatterns = [
	url(r'^register/',views.register,name='register'),
	url(r'^personal/$',views.info,name='info'),
	url(r'^change/$',views.change,name='change'),
	url(r'^accounts/login/$',views.logout,name='logout'),
	url(r'^ajax_captcha/',views.ajax_captcha,name='ajax_captcha'),
	url(r'^login/',views.login_user,name='login')
]
