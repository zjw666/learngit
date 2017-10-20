from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article

def home(request):
	return render(request,'index.html')

def index(request):
	article_list=Article.objects.all().order_by('-time')
	return render(request,'news.html',context={
		'article_list':article_list
	})

def detail(request,pk):
	post=get_object_or_404(Article,pk=pk)
	length=len(Article.objects.all())
	if int(pk)>1:
		post_pre=get_object_or_404(Article,pk=str((int(pk)-1))).title
	else:
		post_pre=""
	if int(pk)<length:
		post_next=get_object_or_404(Article,pk=str((int(pk)+1))).title
	else:
		post_next=""
	return render(request,'content.html',context={'post':post,'length':length,'post_pre':post_pre,'post_next':post_next})