# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swipebuy_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainimage',
            name='main_img',
        ),
        migrations.RemoveField(
            model_name='mainimage',
            name='stuff_id',
        ),
        migrations.RenameField(
            model_name='checkin',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='stuff_id',
            new_name='stuff',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='stuff_id',
            new_name='stuff',
        ),
        migrations.RenameField(
            model_name='stuff',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='swipeaction',
            old_name='stuff_id',
            new_name='stuff',
        ),
        migrations.RenameField(
            model_name='swipeaction',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='latest',
        ),
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.RemoveField(
            model_name='message',
            name='private',
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='message_recipients', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='stuff',
            name='main_img',
            field=models.OneToOneField(related_name='main_image', null=True, blank=True, to='swipebuy_app.Image'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='image',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='bid',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='buy_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='swipeaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='swipeaction',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='MainImage',
        ),
    ]
