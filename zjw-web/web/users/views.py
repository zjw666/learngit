from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,ChangeForm
from .models import User

def register(request):
	redirect_to = request.POST.get('next', request.GET.get('next', ''))
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			if redirect_to:
				return redirect(redirect_to)
			else:
				return redirect('/')
	else:
		form = RegisterForm()
	return render(request,'register.html',context={'form':form,'next':redirect_to})
	
def info(request):
	name = request.POST.get('name', request.GET.get('name', ''))
	if name:
		user1 = User.objects.get(username__exact=name)
		return render(request,'personal.html',context={'user1':user1})
	else:
		return redirect('/')

def change(request):
	name = request.POST.get('personal_name', request.GET.get('personal_name', ''))
	name1 = request.user.username
	if name and (name==name1):
		if request.method == 'POST':
			form = ChangeForm(request.POST)
			if form.is_valid():
				form.save
				return render(request,'change_done.html')
		else:
			user = get_object_or_404(User,username=name)
			form = ChangeForm(instance=user)
		return render(request,'change.html',context={'form':form})
	else:
		return redirect('/')
		
	
	

			
