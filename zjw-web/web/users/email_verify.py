# -*- coding: utf-8 -*-
from .models import EmailVerify,User
from django.core.mail import send_mail
from django.conf import settings

import uuid

def send_register_email(user):
	email_record = Email_Verify()
	email_record.code = str(uuid.uuid1())
	email_record.user = user
	email_record.save()
	title = '账号邮箱激活'
	message = '尊敬的用户：/n欢迎您注册本网站，请点击链接激活邮箱：http:////127.0.0.1:8000//active_check//%s /n 海洋地质办公室201网站管理员ZJW' % email_record.code
	send_result = send_mail(title,message,settings.DEFAULT_FROM_EMAIL,[user.email],fail_silently=True)
	return send_result