from django.conf.urls import url
from . import views

app_name='comments'
urlpatterns = [
	url(r'^comment/$',views.contact,name='contact'),
	url(r'^reply_ajax/',views.reply_ajax,name='reply_ajax'),
	url(r'^email_actived_check/',views.email_actived_check,name='email_actived_check'),
]
