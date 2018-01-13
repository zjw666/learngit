from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .oauth_client import OAuth_GITHUB
from .models import OAuth_ex
from django.contrib.auth import login as auth_login
from users.models import User

import time,uuid,os
	
def git_login(request):
	oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID,GITHUB_KEY,GITHUB_CALLBACK_URL)
	url = oauth_git.get_auth_url()
	return HttpResponseRedirect(url)

def git_check(request):
	request_code = request.GET.get('code')
	oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID,GITHUB_KEY,GITHUB_CALLBACK_URL)
	try:
		access_token = oauth_git.get_access_token(request_code)
		time.sleep(0.1)
	except:
		print("登录错误")
	infos = oauth_git.get_user_info()
	nickname = infos.get('login','')
	open_id = str(oauth_git.openid)
	githubs = OAuth_ex.objects.filter(openid=open_id,type=1)
	if githubs:
		auth_login(request,githubs[0].user,backend='django.contrib.auth.backends.ModelBackend')
		return HttpResponseRedirect('/')
	else:
		try:
			email = oauth_git.get_email()
		except:
			print("获取不到邮箱")
			return HttpResponseRedirect('/')
	users = User.objects.filter(email=email)
	if users:
		user = users[0]
	else:
		user = User(username=nickname,email=email,sex='1')
		pwd = str(uuid.uuid1())
		user.set_password(pwd)
		user.is_active = True
		user.save()
	oauth_ex = OAuth_ex(user = user,openid = open_id,type=1)
	oauth_ex.save()
	auth_login(request,githubs[0].user,backend='django.contrib.auth.backends.ModelBackend')
	print("登录并绑定成功")
	return HttpResponseRedirect('/')
	
def bind_email(request):
	pass
