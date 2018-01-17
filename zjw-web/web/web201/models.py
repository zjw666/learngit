# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

class Category(models.Model):   #文章分类类型
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
	
class Article(models.Model):    #文章
	title = models.CharField(max_length=100)
	content = models.TextField()
	time = models.DateTimeField()
	author = models.CharField(max_length=20)
	category = models.ForeignKey(Category)
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):   #获取文章的url
		return reverse('web201:detail',kwargs={'type':self.category.name,'pk':self.pk})
		
	def increase_views(self,request):  #点赞
		try:
			request.COOKIES["article_%s_readed" % self.id]
		except:
			self.views += 1
			self.save(update_fields=['views'])

