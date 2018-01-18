# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm,ReplyForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from users.models import User
from django.core.mail import send_mail
from django.conf import settings

def contact(request): #联系页
	if request.method == 'POST':
		if request.user.username:
			form = CommentForm(request.POST)
			if form.is_valid():
				form.save()
				form = CommentForm()
				comment_list = Comment.objects.all().filter(public = True).order_by('id').reverse()
				if len(comment_list) > 5:
					data,comment_list=comment_paginator(request,comment_list)
				else:
					data=''
				response = True
				context = {'form':form,'comment_list':comment_list,'response':response,'data':data}
				return render(request,'contact.html',context=context)
	else:
		form = CommentForm()
	comment_list = Comment.objects.all().filter(public = True).order_by('id').reverse()
	if len(comment_list) > 5:
		(data,comment_list)=comment_paginator(request,comment_list)
	else:
		data=''
	context = {'form':form,'comment_list':comment_list,'data':data}
	return render(request,'contact.html',context=context)

def reply_ajax(request):
	if request.is_ajax():
		form = ReplyForm(request.POST)
		if form.is_valid():
			reply = form.save()
			reply_to = User.objects.filter(username=request.POST.get("reply_to"))
			reply_to_name = reply_to[0].username
			reply_comment_name = reply.comment.author.username
			email_title = '回复提醒'
			if reply.comment.important:
				if reply_comment_name != reply.author.username:
					email_message1 = '''尊敬的%s用户:
					
    %s用户回复了你在关于"%.10s"下的评论，赶快去看看吧！
											
    海洋地质办公室唯一官网：http://127.0.0.1:8000/
										
                                         海洋地质办公室201网站管理员ZJW''' % (reply_comment_name,reply.author.username,reply.comment.content)
					send_mail(email_title,email_message1,settings.DEFAULT_FROM_EMAIL,[reply.comment.author.email],fail_silently=True)
				if reply_to_name != reply_comment_name:
					email_message2 = '''尊敬的%s用户:
					
    %s用户回复了你在关于"%.10s"下的评论，赶快去看看吧！
											
    海洋地质办公室唯一官网：http://127.0.0.1:8000/
										
                                         海洋地质办公室201网站管理员ZJW''' % (reply_to_name,reply.author.username,reply.comment.content)
					send_mail(email_title,email_message2,settings.DEFAULT_FROM_EMAIL,[reply_to[0].email],fail_silently=True)		
			data = {'reply_status':1,'reply_id':reply.id,'url':reply.author.pic.url,'author_name':reply.author.username,'time':reply.created_time}
		else:
			data = {'reply_status':0}
	return JsonResponse(data)	

def email_actived_check(request):
	if request.is_ajax():
		author = request.GET.get('author')
		users = User.objects.filter(id=author)
		if users and hasattr(users[0],'emailverify') and users[0].emailverify.actived:
			data = {'status':0}
		else:
			data = {'status':1}
	return JsonResponse(data)
		
		
def comment_paginator(request,comment_list):
	p = Paginator(comment_list,5)   #分页
	page = int(request.GET.get('page',1))
	comment_list = p.page(page)
	left = []
	right = []
	left_has_more = False
	right_has_more = False
	first = False
	last = False
	total_pages = p.num_pages
	page_range = p.page_range
	if page == 1:
		right = page_range[page:page+2]
		if right[-1] < total_pages - 1:
			right_has_more = True
		if right[-1] < total_pages:
			last = True
	elif page == total_pages:
		left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
		if left[0] > 2:
			left_has_more = True
		if left[0] > 1:
			first = True
	else:
		left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
		right = page_range[page:page+2]
		if left[0] > 2:
			left_has_more = True
		if left[0] > 1:
			first = True
		if right[-1] < total_pages - 1:
			right_has_more = True
		if right[-1] < total_pages:
			last = True
	data = {
		'left':left,
		'right':right,
		'left_has_more':left_has_more,
		'right_has_more':right_has_more,
		'first':first,
		'last':last,
		'total_pages':total_pages,
		'page':page
	}
	return (data,comment_list)

	
