# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-25 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171223_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='zjw.jpg', upload_to='pic'),
        ),
    ]