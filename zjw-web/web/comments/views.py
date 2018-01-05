from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm,ReplyForm
from django.http import JsonResponse
from django.core.paginator import Paginator

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
			data = {'reply_status':1,'reply_id':reply.id,'url':reply.author.pic.url,'author_name':reply.author.username,'time':reply.created_time}
		else:
			data = {'reply_status':0}
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

