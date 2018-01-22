# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError

CHOICES=(('1','男'),('2','女'))
class RegisterForm(UserCreationForm):  #注册表单
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的用户名",'required':'required','oninvalid':"setCustomValidity('请输入你的用户名');",'oninput':"setCustomValidity('');"}))
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES)
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':"请输入你的电子邮箱地址",'required':'required','oninvalid':"setCustomValidity('请输入你的电子邮箱地址');",'oninput':"setCustomValidity('');"}))
	signature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的个性签名"}),required=False)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"请设置你的密码",'required':"required",'oninvalid':"setCustomValidity('请设置你的密码');",'oninput':"setCustomValidity('');"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"请重新输入你的密码",'required':"required",'oninvalid':"setCustomValidity('请重新输入你的密码');",'oninput':"setCustomValidity('');"}))
	captcha = CaptchaField(error_messages={"invalid":u"验证码错误","required":u"请输入验证码"},required=True)
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username","email","signature","sex")

class ChangeForm(forms.ModelForm):   #个人信息更改表单
	pic = forms.ImageField(widget=forms.FileInput(attrs={'accept':"image/*",'oninvalid':"setCustomValidity('请上传图片');",'oninput':"setCustomValidity('');"}),required=False)
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES)
	signature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的个性签名"}),required=False)
	hobby = forms.CharField(widget=forms.Textarea(attrs={'maxlength':'300','class':'form-control','placeholder':"请输入你的爱好"}),required=False)
	class Meta:
		model = User
		fields = ['pic','sex','signature','hobby']
	
	def clean_pic(self):
		pic = self.cleaned_data['pic']
		if pic._size/1024/1024 > 1:
			raise ValidationError(u'上传图片大小不能超过1M')
		else:
			return pic

class LoginForm(AuthenticationForm):  #登录表单
	captcha = CaptchaField(error_messages={"invalid":u"验证码错误","required":u"请输入验证码"},required=True)