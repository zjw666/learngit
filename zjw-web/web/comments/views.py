from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm

def contact(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/contact?response=True')
		else:
			comment_list = Comment.objects.all().order_by('-created_time')
			context = {'form':form,'comment_list':comment_list}
			return render(request,'contact.html',context=context)
	return redirect('/contact/')		

