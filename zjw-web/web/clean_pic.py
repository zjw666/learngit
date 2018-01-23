import django
from django.conf import settings


import os

def load_setting():
	os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'
	django.setup()

def main():
	load_setting()
	from users.models import User
	
	img_folder = os.path.join(settings.MEDIA_ROOT,'pic')
	img_del_num = 0
	img_count = 0
	
	for root,dirs,files in os.walk(img_folder):
		for filename in files:
			if User.objects.filter(pic__contains = filename).count() == 0:
				img_path = os.path.join(root,filename)
				os.remove(img_path)
				img_del_num += 1
			img_count += 1
	
	print("共有%s张图片，其中%s张图片已不再使用，已经删除" % (img_count,img_del_num))
				
	
if __name__ == '__main__':
    main()	