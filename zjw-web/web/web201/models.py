from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
	
class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	time = models.DateTimeField()
	author = models.CharField(max_length=20)
	category = models.ForeignKey(Category)
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('web201:detail',kwargs={'pk':self.pk})

