from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm

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

