from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
	article_list=Article.objects.all().order_by('-time')
	return render(request,'news.html',context={
		'article_list':article_list
	})

def detail(request,pk):
	post=get_object_or_404(Article,pk=pk)
	length=len(Article.objects.all())
	return render(request,'content.html',context={'post':post,'length':length})