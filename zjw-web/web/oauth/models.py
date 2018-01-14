from django.db import models
from users.models import User


type=(
	('1','github'),
	('2','qq'),
	('3','weibo')
)
class OAuth_ex(models.Model):
	user = models.ForeignKey(User)
	openid = models.CharField(max_length=100,default='')
	type = models.CharField(max_length=1,choices=type)
	
	def __unicode__(self):
		return u'(%s)' % (self.user)
