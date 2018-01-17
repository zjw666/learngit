from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from .oauth_client import OAuth_GITHUB,OAuth_QQ,OAuth_WEIBO
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
	if not signature:
		signature = "无个性签名"
	sex = '1'
	githubs = OAuth_ex.objects.filter(openid=open_id,type=type)
	if githubs:
		auth_login(request,githubs[0].user,backend='django.contrib.auth.backends.ModelBackend')
		return HttpResponseRedirect('/')
	else:
		try:
			email = oauth_git.get_email()
		except:
			url = "%s?nickname=%s&openid=%s&type=%s&signature=%s&image_url=%s&sex=%s" % (reverse('oauth:bind_email'),nickname,open_id,type,signature,image_url,sex)
			return HttpResponseRedirect(url)
	users = User.objects.filter(email=email)
	if users:
		user = users[0]
	else:
		while User.objects.filter(username=nickname):
			nickname = nickname + '*'
		user = User(username=nickname,email=email,sex=sex,signature=signature)
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
	
def qq_login(request):
	oauth_qq = OAuth_QQ(settings.QQ_APP_ID,settings.QQ_KEY,settings.QQ_CALLBACK_URL)
	url = oauth_qq.get_auth_url()
	return HttpResponseRedirect(url)
	
def qq_check(request):
	type = 2
	code = request.GET.get('code','')
	oauth_qq = OAuth_QQ(settings.QQ_APP_ID,settings.QQ_KEY,settings.QQ_CALLBACK_URL)
	try:
		access_token = oauth_qq.get_access_token(code)
		time.sleep(0.1)
	except:
		data={}
		data['goto_url'] = '/'
		data['goto_time'] = 10000
		data['goto_page'] = True
		data['message_title'] = '登录失败'
		data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
		return render_to_response('oauth/response.html',data)
	openid = oauth_qq.get_open_id()
	qqs = OAuth_ex.objects.filter(openid=openid,type=type)
	if qqs:
		auth_login(request,qqs[0].user,backend='django.contrib.auth.backends.ModelBackend')
		return HttpResponseRedirect('/')
	else:
		infos = oauth_qq.get_user_info()
		nickname = infos.get('nickname','')
		image_url = infos.get('figureurl_qq_1','')
		sex = '1' if infos.get('gender','') == '男' else '2'
		signature = '无个性签名'
		url = "%s?nickname=%s&openid=%s&type=%s&signature=%s&image_url=%s&sex=%s" % (reverse('oauth:bind_email'),nickname,openid,type,signature,image_url,sex)
		return HttpResponseRedirect(url)
		
def weibo_login(request):
	oauth_weibo = OAuth_WEIBO(settings.WEIBO_APP_ID,settings.WEIBO_KEY,settings.WEIBO_CALLBACK_URL)
	url = oauth_weibo.get_auth_url()
	return HttpResponseRedirect(url)

def weibo_check(request):
	type = 3
	code = request.GET.get('code','')
	oauth_weibo = OAuth_WEIBO(settings.WEIBO_APP_ID,settings.WEIBO_KEY,settings.WEIBO_CALLBACK_URL)
	try:
		oauth_weibo.get_access_token(code)
		time.sleep(0.1)
	except:
		data={}
		data['goto_url'] = '/'
		data['goto_time'] = 10000
		data['goto_page'] = True
		data['message_title'] = '登录失败'
		data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
		return render_to_response('oauth/response.html',data)
	openid = oauth_weibo.get_open_id()
	weibos = OAuth_ex.objects.filter(openid=openid,type=type)
	if weibos:
		auth_login(request,weibos[0].user,backend='django.contrib.auth.backends.ModelBackend')
		return HttpResponseRedirect('/')
	else:
		try:
			email = oauth_weibo.get_email()
		except:
			infos = oauth_weibo.get_user_info()
			nickname = infos.get('screen_name','')
			image_url = infos.get('avatar_large','')
			signature = infos.get('description','')
			if not signature:
				signature = "无个性签名"
			print("signature="+signature)
			sex = '2' if infos.get('gender','') == 'f' else '1'
			url = "%s?nickname=%s&openid=%s&type=%s&signature=%s&image_url=%s&sex=%s" % (reverse('oauth:bind_email'),nickname,openid,type,signature,image_url,sex)
			return HttpResponseRedirect(url)
	users = User.objects.filter(email=email)
	if users:
		user = users[0]
	else:
		while User.objects.filter(username=nickname):
			nickname = nickname + '*'
		user = User(username=nickname,email=email,sex=sex,signature=signature)
		pwd = str(uuid.uuid1())
		user.set_password(pwd)
		user.is_active = True
		user.download_image(image_url,nickname)
		user.save()
	oauth_ex = OAuth_ex(user = user,openid = openid,type=type)
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
	sex = request.GET.get('sex',request.POST.get('sex',''))
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
			sex = form.cleaned_data['sex']
			users = User.objects.filter(email = email)
			if users:
				user = users[0]
			else:
				while User.objects.filter(username=nickname):
					nickname = nickname + '*'
				user = User(username=nickname,email=email,sex=sex,signature=signature)
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
			'sex':sex,
		})
	return render(request,'oauth/form.html',context={'form':form,'nickname':nickname,'type':type})	
