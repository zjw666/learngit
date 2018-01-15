# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,ChangeForm,LoginForm
from .models import User,EmailVerify
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import JsonResponse
from django.contrib.auth import login as auth_login,authenticate
from django.core.mail import send_mail
from django.conf import settings

import uuid

def register(request):  #注册
	redirect_to = request.POST.get('next', request.GET.get('next', ''))
	name = request.POST.get('username')
	hashkey = CaptchaStore.generate_key()   #生成验证码秘钥
	image_url = captcha_image_url(hashkey)  #生成验证码图片
	email_already_exist = False
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		email_address = request.POST.get('email','')
		try:                                           #验证邮箱是否已经存在
			get_object_or_404(User,email=email_address)
			email_already_exist = True
		except:
			if form.is_valid():
				human = True
				user = form.save()
				auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend') #注册成功后立即登录
				if redirect_to:
					return redirect(redirect_to)   #跳转至注册前页面
				else:
					return redirect('/')
	else:
		form = RegisterForm()
	return render(request,'register.html',context={'form':form,'next':redirect_to,'hashkey':hashkey,'image_url':image_url,'email_already_exist':email_already_exist})

def login_user(request):  #登录
	redirect_to = request.POST.get('next', request.GET.get('next', ''))
	if request.method == "POST":
		form = LoginForm(request,data=request.POST)
		form.error_messages={'invalid_login': ("用户不存在或密码不正确，请注意它们都是区分大小写的")}
		if form.is_valid():
			auth_login(request,form.get_user())
			if redirect_to:
				return redirect(redirect_to)   #跳转至登录前页面
			else:
				return redirect('/')
	else:
		form = LoginForm()
	return render(request,'registration/login.html',context={'form':form})
	
	
def info(request):    #查看个人信息
	name = request.POST.get('name', request.GET.get('name', ''))
	if name:
		user1 = User.objects.get(username__exact=name)
		return render(request,'personal.html',context={'user1':user1})
	else:
		return redirect('/')

def change(request):  #修改个人信息
	name = request.user.username
	if name:
		if request.method == 'POST':
			user = get_object_or_404(User,username=name)
			form = ChangeForm(request.POST,request.FILES,instance=user)
			if form.is_valid():
				form.save()
				return render(request,'change_done.html')
		else:
			form = ChangeForm(instance=request.user)
		return render(request,'change.html',context={'form':form})
	else:
		return redirect('/')

def logout(request):  #注销
	return redirect('/')
	
def ajax_captcha(request):  #验证码输入验证
	if request.is_ajax():
		result = CaptchaStore.objects.filter(response=request.GET.get('response'),hashkey=request.GET.get('hashkey'))
		if result:
			data={'status':1}
		else:
			data={'status':0}
		return JsonResponse(data)
		
def active(request):
	if request.user.is_authenticated():
		email_record = EmailVerify.objects.filter(user=request.user)
		print("这里")
		if not email_record:
			email_record = EmailVerify(code=str(uuid.uuid1()),user=request.user)
			email_record.save()
			email_title = '账号邮箱激活'
			email_message = '''尊敬的用户:
			
							    欢迎您访问海洋地质办公室201网站.
								
							    请点击链接激活账号邮箱：http://127.0.0.1:8000/active_check/%s
								
							    海洋地质办公室201网站管理员ZJW''' % email_record.code
			send_result = send_mail(email_title,email_message,settings.DEFAULT_FROM_EMAIL,[request.user.email],fail_silently=False)
			if send_result:
				print("发送成功")
			else:
				print("发送失败")
	return redirect('/')
				
			
		