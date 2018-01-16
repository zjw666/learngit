# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):   #首页
	articles = Article.objects.all().order_by('-time')[0:4]
	if articles:
		first_article = articles[0]
		other_articles = articles[1:]
	else:
		first_article = []
		other_articles = []
	return render(request,'index.html',context={'first_article':first_article,'other_articles':other_articles})
	
def introduction(request):    #介绍页
	return render(request,'introduction.html')
	
def teachers(request,name):  #老师页
	if name=='li':
		return render(request,'teachers-li.html')
	if name=='wang':
		return render(request,'teachers-wang.html')

def students(request):  #学生页
	return render(request,'students.html')

def news(request,type):   #新闻页
	articles = Article.objects.filter(category__name = type).order_by('-time')
	p = Paginator(articles,10)   #分页，10篇文章一页
	if p.num_pages <= 1:
		article_list = articles
		data = ''
	else:
		page = int(request.GET.get('page',1))
		article_list = p.page(page)
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
	return render(request,'news.html',context={
		'article_list':article_list,'data':data
	})


def detail(request,type,pk):   #文章内容页
	post=get_object_or_404(Article,pk=pk)
	post.increase_views()
	article_list=Article.objects.filter(category__name = type).order_by('-time')
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

def search(request):   #搜索页
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "请输入关键词"
		return render(request,'search.html',context={'error_msg':error_msg})
	article_list = Article.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
	return render(request,'search.html',context={'error_msg':error_msg,'article_list':article_list})