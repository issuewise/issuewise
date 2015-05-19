# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('activity_status', model_utils.fields.StatusField(default=b'I', max_length=100, no_check_for_status=True, choices=[(b'I', b'inactive'), (b'A', b'active')])),
                ('explanation', model_utils.fields.StatusField(default=b'NE', max_length=100, no_check_for_status=True, choices=[(b'NE', b'no explanation'), (b'NV', b'not verified'), (b'AB', b'account blocked'), (b'AD', b'account deactivated')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor=b'activity_status')),
                ('name', models.CharField(help_text='Required. 200 characters or fewer.', max_length=200, verbose_name='full name')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'wise user',
                'verbose_name_plural': 'wise users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseActivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('uuid', models.CharField(max_length=100, verbose_name='unique id')),
                ('creator', models.ForeignKey(related_name=b'accounts_wiseactivation_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseFriendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folllowed_at', models.DateTimeField(auto_now_add=True, verbose_name='time followed')),
                ('status', models.CharField(blank=True, max_length=5, null=True, verbose_name='friendship status', choices=[(b'F', b'Friends'), (b'R', b'Friend Request Sent')])),
                ('followee', models.ForeignKey(related_name=b'accounts_wisefriendship_followee', verbose_name='followee', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(related_name=b'accounts_wisefriendship_follower', verbose_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
