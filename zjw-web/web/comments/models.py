from django.db import models
from users.models import User

class Base(models.Model):
	author = models.ForeignKey(User)
	content = models.TextField(max_length=500)
	created_time = models.DateField(auto_now = True)
	def __str__(self):
		return self.content[:20]
	class Meta:
		abstract = True

class Comment(Base):
	public = models.BooleanField(default=True)
	important = models.BooleanField(default=False)
	
class Reply(Base):
	comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
