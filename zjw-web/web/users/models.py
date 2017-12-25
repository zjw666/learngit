# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

SEX = (
	('1','boy'),
	('2','girl'),
)

class User(AbstractUser):
	pic = models.ImageField(upload_to='pic',default="zjw.jpg")
	signature = models.CharField(max_length=50,blank=True,default="无个性签名")
	sex = models.CharField(max_length=1,choices=SEX)
	hobby = models.TextField(max_length=200,blank=True,default="无")
	class Meta(AbstractUser.Meta):
		pass