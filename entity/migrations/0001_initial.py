# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('type_status', models.CharField(default=b'NULL', max_length=2, choices=[(b'ST', b'student'), (b'TC', b'teacher'), (b'SF', b'staff')])),
                ('praise_count', models.IntegerField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=80)),
                ('position_x', models.CharField(max_length=10)),
                ('position_y', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonalNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('pub_time', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(blank=True, to='entity.Department', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=10)),
                ('reference_count', models.IntegerField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card', models.ForeignKey(to='entity.Card')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personalnotice',
            name='author',
            field=models.ForeignKey(to='entity.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.ManyToManyField(to='entity.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='tags',
            field=models.ManyToManyField(to='entity.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='location',
            field=models.ForeignKey(blank=True, to='entity.Location', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(to='entity.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
