# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiseGroupCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('creator', models.ForeignKey(related_name=b'categories_wisegroupcategory_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name=b'categories_wisegroupcategory_owner', verbose_name='group which owns this category', to='groups.WiseGroup')),
            ],
            options={
                'verbose_name': 'group category',
                'verbose_name_plural': 'group categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WisePublicCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('creator', models.ForeignKey(related_name=b'categories_wisepubliccategory_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'public category',
                'verbose_name_plural': 'public categories',
            },
            bases=(models.Model,),
        ),
    ]
