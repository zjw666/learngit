# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

CHOICES=(('1','男'),('2','女'))
class RegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的用户名",'required':'required','oninvalid':"setCustomValidity('请输入你的用户名');",'oninput':"setCustomValidity('');"}))
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES)
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':"请输入你的电子邮箱地址",'required':'required','oninvalid':"setCustomValidity('请输入你的电子邮箱地址');",'oninput':"setCustomValidity('');"}))
	signature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的个性签名"}),required=False)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"请设置你的密码",'required':"required",'oninvalid':"setCustomValidity('请设置你的密码');",'oninput':"setCustomValidity('');"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"请重新输入你的密码",'required':"required",'oninvalid':"setCustomValidity('请重新输入你的密码');",'oninput':"setCustomValidity('');"}))
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username","email","signature","sex")

class ChangeForm(forms.ModelForm):
	pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':"请上传图片",'required':"required",'oninvalid':"setCustomValidity('请上传图片');",'oninput':"setCustomValidity('');"}),required=False)
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES)
	signature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的个性签名"}),required=False)
	hobby = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':"请输入你的爱好"}),required=False)
	class Meta:
		model = User
		fields = ['pic','sex','signature','hobby']