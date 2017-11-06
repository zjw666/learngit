from django import forms
from .models import Comment

CHOICES=(('1','男'),('2','女'))
class CommentForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入你的姓名",'required':'required','oninvalid':"setCustomValidity('请输入你的姓名');",'oninput':"setCustomValidity('');"}))
	birth = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control",'placeholder':"请输入你的出生年月，例如：1994/06/06"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':"请输入你的电子邮箱地址",'required':'required','oninvalid':"setCustomValidity('请输入你的电子邮箱地址');",'oninput':"setCustomValidity('');"}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'required':'required','oninvalid':"setCustomValidity('请输入你要发送的信息');",'oninput':"setCustomValidity('');"}))
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES)
	class Meta:
		model = Comment
		fields = ['name','email','sex','birth','content','public','important']