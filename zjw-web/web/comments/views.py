from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm,ReplyForm
from django.http import JsonResponse

def contact(request): #联系页
	comment_list = Comment.objects.all().filter(public = True).order_by('-created_time')
	if request.method == 'POST':
		if request.user.username:
			form = CommentForm(request.POST)
			if form.is_valid():
				form.save()
				response = True
				context = {'form':form,'comment_list':comment_list,'response':response}
				return render(request,'contact.html',context=context)
	else:
		form = CommentForm()
	context = {'form':form,'comment_list':comment_list}
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
		
		

