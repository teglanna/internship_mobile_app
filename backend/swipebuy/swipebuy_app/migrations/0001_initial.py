# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('latest', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('url', models.URLField()),
                ('image', models.ImageField(height_field=300, width_field=300, upload_to=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('main_img', models.OneToOneField(to='swipebuy_app.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('text', models.TextField(max_length=500)),
                ('private', models.BooleanField(default=False)),
                ('bid', models.IntegerField(blank=True)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('id', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.CharField(max_length=500)),
                ('pickup', models.BooleanField(default=False)),
                ('delivery', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('buy_time', models.DateField(default=datetime.date.today)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SwipeAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('action', models.IntegerField(choices=[(1, b'swiping'), (2, b'make_bid'), (3, b'buy')])),
                ('stuff_id', models.ForeignKey(to='swipebuy_app.Stuff')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='message',
            name='stuff_id',
            field=models.ForeignKey(to='swipebuy_app.Stuff'),
        ),
        migrations.AddField(
            model_name='mainimage',
            name='stuff_id',
            field=models.ForeignKey(to='swipebuy_app.Stuff'),
        ),
        migrations.AddField(
            model_name='image',
            name='stuff_id',
            field=models.ForeignKey(to='swipebuy_app.Stuff'),
        ),
    ]
