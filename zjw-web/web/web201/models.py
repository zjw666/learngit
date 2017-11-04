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
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('web201:detail',kwargs={'type':self.category.name,'pk':self.pk})
		
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

