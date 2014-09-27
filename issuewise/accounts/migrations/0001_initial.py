# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WiseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(help_text='Required. 200 characters or fewer.', max_length=200, verbose_name='full name')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('activity_status', model_utils.fields.StatusField(default=b'I', max_length=100, no_check_for_status=True, choices=[(b'I', b'inactive'), (b'A', b'active')])),
                ('explanation', model_utils.fields.StatusField(default=b'NV', max_length=100, no_check_for_status=True, choices=[(b'NV', b'not verified'), (b'AB', b'account blocked'), (b'AD', b'account deleted')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor=b'activity_status')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'wise user',
                'verbose_name_plural': 'wise users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationalInstitutions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFollowUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folllowed_at', models.DateTimeField(auto_now_add=True, verbose_name='time followed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
                ('designation', models.CharField(max_length=100, null=True, verbose_name='official position held by user', blank=True)),
                ('autobiographer', models.ForeignKey(related_name=b'accounts_work_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
