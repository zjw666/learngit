from django import forms
from .models import Comment,Reply
from captcha.fields import CaptchaField
from users.models import EmailVerify
from django.core.exceptions import ValidationError

CHOICES=(('1','男'),('2','女'))
class CommentForm(forms.ModelForm):
	content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':"form-control",'required':'required','placeholder':'请输入评论的内容','oninvalid':"setCustomValidity('请输入你要发送的信息');",'oninput':"setCustomValidity('');"}))
	captcha = CaptchaField(error_messages={"invalid":u"验证码错误","required":u"请输入验证码"},required=True)
	class Meta:
		model = Comment
		fields = ['content','public','important','author']
		
	def clean_content(self):
		content = self.cleaned_data.get('content')
		if content:
			return content
		else:
			raise ValidationError(u'内容不能为空')

		
class ReplyForm(forms.ModelForm):
	content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':"form-control",'required':'required','oninvalid':"setCustomValidity('请输入你要回复的内容');",'oninput':"setCustomValidity('');"}))
	class Meta:
		model = Reply
		fields = ['content','author','comment','reply_to']
		
	def clean_content(self):
		content = self.cleaned_data.get('content')
		if content:
			return content
		else:
			raise ValidationError(u'内容不能为空')