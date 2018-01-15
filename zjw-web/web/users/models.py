# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.files import File 

import urllib

SEX = (
	('1','boy'),
	('2','girl'),
)

class User(AbstractUser):       #自定义用户模型
	pic = models.ImageField(upload_to='pic',default="zjw.jpg")
	signature = models.CharField(max_length=50,blank=True,default="无个性签名")
	sex = models.CharField(max_length=1,choices=SEX)
	hobby = models.TextField(max_length=200,blank=True,default="无")
	class Meta(AbstractUser.Meta):
		pass
	
	def download_image(self,image_url,name):    #1
		result = urllib.request.urlretrieve(image_url)
		self.pic.save(name,File(open(result[0],'rb')))
		

class EmailVerify(models.Model):
	code = models.CharField(max_length=50)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	send_time = models.DateTimeField(auto_now_add=True)
	actived = models.BooleanField(default = False)
	
	def __unicode__(self):
		return (self.user.email,self.actived)