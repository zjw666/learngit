from django.contrib import admin
from .models import User,EmailVerify

admin.site.register(User)
admin.site.register(EmailVerify)
