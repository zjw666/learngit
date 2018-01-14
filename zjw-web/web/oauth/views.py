from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from .oauth_client import OAuth_GITHUB
from .models import OAuth_ex
from django.contrib.auth import login as auth_login
from users.models import User
from django.core.urlresolvers import reverse
from .forms import BindEmail

import time,uuid
	
def git_login(request):
	oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID,settings.GITHUB_KEY,settings.GITHUB_CALLBACK_URL)
	url = oauth_git.get_auth_url()
	return HttpResponseRedirect(url)

def git_check(request):
	type='1'
	request_code = request.GET.get('code')
	oauth_git = OAuth_GITHUB(settings.GITHUB_APP_ID,settings.GITHUB_KEY,settings.GITHUB_CALLBACK_URL)
	try:
		access_token = oauth_git.get_access_token(request_code)
		time.sleep(0.1)
	except:
		data={}
		data['goto_url'] = '/'
		data['goto_time'] = 10000
		data['goto_page'] = True
		data['message_title'] = '登录失败'
		data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
		return render_to_response('oauth/response.html',data)
	infos = oauth_git.get_user_info()
	nickname = infos.get('login','')
	image_url = infos.get('avatar_url','')
	open_id = str(oauth_git.openid)
	signature = infos.get('bio','')
	githubs = OAuth_ex.objects.filter(openid=open_id,type=type)
	if githubs:
		auth_login(request,githubs[0].user,backend='django.contrib.auth.backends.ModelBackend')
		return HttpResponseRedirect('/')
	else:
		try:
			print(abc)
			email = oauth_git.get_email()
		except:
			url = "%s?nickname=%s&openid=%s&type=%s&signature=%s&image_url=%s" % (reverse('oauth:bind_email'),nickname,open_id,type,signature,image_url)
			return HttpResponseRedirect(url)
	users = User.objects.filter(email=email)
	if users:
		user = users[0]
	else:
		while User.objects.filter(username=nickname):
			nickname = 'github_'+nickname
		user = User(username=nickname,email=email,sex='1',signature=signature)
		pwd = str(uuid.uuid1())
		user.set_password(pwd)
		user.is_active = True
		user.download_image(image_url,nickname)
		user.save()
	oauth_ex = OAuth_ex(user = user,openid = open_id,type=type)
	oauth_ex.save()
	auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
	data={}
	data['goto_url'] = '/'
	data['goto_time'] = 10000
	data['goto_page'] = True
	data['message_title'] = '绑定用户成功'
	data['message'] = u'绑定成功！您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' % nickname
	return render_to_response('oauth/response.html',data)
	
def bind_email(request):
	openid = request.GET.get('openid',request.POST.get('openid',''))
	nickname = request.GET.get('nickname',request.POST.get('nickname',''))
	type = request.GET.get('type',request.POST.get('type',''))
	signature = request.GET.get('signature',request.POST.get('signature',''))
	image_url = request.GET.get('image_url',request.POST.get('image_url',''))
	if request.method == 'POST':
		form = BindEmail(request.POST)
		if form.is_valid():
			openid = form.cleaned_data['openid']
			nickname = form.cleaned_data['nickname']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			type = form.cleaned_data['type']
			signature = form.cleaned_data['signature']
			image_url = form.cleaned_data['image_url']
			users = User.objects.filter(email = email)
			if users:
				user = users[0]
			else:
				while User.objects.filter(username=nickname):
					nickname = 'github_'+nickname
				user = User(username=nickname,email=email,sex='1',signature=signature)
				user.set_password(password)
				user.is_active = True
				user.download_image(image_url,nickname)
				user.save()
			oauth_ex = OAuth_ex(user=user,openid=openid,type=type)
			oauth_ex.save()
			auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
			data={}
			data['goto_url'] = '/'
			data['goto_time'] = 10000
			data['goto_page'] = True
			data['message_title'] = '绑定账号成功'
			data['message'] = u'绑定成功！您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' % nickname
			return render_to_response('oauth/response.html',data)
	else:
		form = BindEmail(initial={
			'openid':openid,
			'nickname':nickname,
			'type':type,
			'signature':signature,
			'image_url':image_url,
		})
	return render(request,'oauth/form.html',context={'form':form,'nickname':nickname,'type':type})	
