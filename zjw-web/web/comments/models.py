from django.db import models

SEX = (
	('1','boy'),
	('2','girl'),
)

class Base(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField(max_length=500)
	created_time = models.DateField(auto_now = True)
	def __str__(self):
		return self.content[:20]
	class Meta:
		abstract = True

class Comment(Base):
	email = models.EmailField(max_length=255)
	sex = models.CharField(max_length=1,choices = SEX)
	birth = models.DateField(blank=True,default="1994/06/06")
	public = models.BooleanField(default=True)
	important = models.BooleanField(default=False)
	allow = models.BooleanField(default=False)
	
class Reply(Base):
	comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
