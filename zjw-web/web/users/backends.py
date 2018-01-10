# -*- coding: utf-8 -*-
from .models import User

class EmailBackend(object):  #允许使用邮箱登录
	def authenticate(self,**kwargs):
		email = kwargs.get('email',kwargs.get('username'))
		try:
			user = User.objects.get(email=email)
		except:
			pass
		else:
			if user.check_password(kwargs["password"]):
				return user
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None