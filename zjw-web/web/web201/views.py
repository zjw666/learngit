# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article

def home(request):
	return render(request,'index.html')
	
def introduction(request):
	return render(request,'introduction.html')
	
def teachers(request,name):
	if name=='li':
		return render(request,'teachers-li.html')
	if name=='wang':
		return render(request,'teachers-wang.html')

def students(request):
	return render(request,'students.html')

def news(request,type):
	article_list=Article.objects.all().filter(category__name = type).order_by('-time')
	return render(request,'news.html',context={
		'article_list':article_list
	})

def contact(request):
	return render(request,'contact.html')

def detail(request,type,pk):
	post=get_object_or_404(Article,pk=pk)
	post.increase_views()
	article_list=Article.objects.all().filter(category__name = type).order_by('-time')
	index_list=[]
	for i in range(len(article_list)):
			index_list.append(article_list[i].pk)
	index = index_list.index(int(pk))
	if index <= 0:
		pre=-1
		next = index_list[index+1]
	elif index >= len(index_list)-1:
		next=-1
		pre = index_list[index-1]
	else:
		pre = index_list[index-1]
		next = index_list[index+1]
	if pre == -1:
		pre_title = '这是第一篇新闻了'
	else:
		pre_title=Article.objects.get(id__exact=pre).title
	if next == -1:
		next_title='这是最后一篇新闻了'
	else:
		next_title=Article.objects.get(id__exact=next).title
	return render(request,'content.html',context={'post':post,'pre':pre,'next':next,'pre_title':pre_title,'next_title':next_title})