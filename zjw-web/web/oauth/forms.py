from django import forms
from users.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import OAuth_ex


class BindEmail(forms.Form):
	sex = forms.CharField(widget=forms.HiddenInput(attrs={'id':'sex'}))
	image_url = forms.CharField(widget=forms.HiddenInput(attrs={'id':'image_url'}),required=False)
	signature = forms.CharField(widget=forms.HiddenInput(attrs={'id':'signature'}),required=False)
	type = forms.CharField(widget=forms.HiddenInput(attrs={'id':'type'}))
	openid = forms.CharField(widget=forms.HiddenInput(attrs={'id':'openid'}))
	nickname = forms.CharField(widget=forms.HiddenInput(attrs={'id':'nickname'}))
	email = forms.EmailField(label=u'绑定邮箱',widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':u'请输入用于绑定本站账号的邮箱','oninvalid':"setCustomValidity('请输入正确的邮箱地址');",'oninput':"setCustomValidity('');"}))
	password = forms.CharField(label=u'用户密码',widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':u'若尚未注册过本站账号，则该密码作为账户密码',"oninvalid":"setCustomValidity('请输入绑定用户的密码');",'oninput':"setCustomValidity('');"}))
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		type = self.cleaned_data.get('type')
		users = User.objects.filter(email=email)
		if users:
			if OAuth_ex.objects.filter(user=users[0],type=type):
				raise ValidationError(u'邮箱已经被绑定了')
		return email
		
	def clean_password(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		users = User.objects.filter(email=email)
		if users:
			user = authenticate(email=email,password=password)
			if user:
				return password
			else:
				raise ValidationError(u'密码不正确，绑定失败')
		
		
		