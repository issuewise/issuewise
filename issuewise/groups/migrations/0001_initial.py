# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcribed_at', models.DateTimeField(auto_now_add=True, verbose_name='time subscribed')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(help_text='Required. 200 characters or less.', max_length=200, verbose_name='group name')),
                ('creator', models.OneToOneField(related_name=b'creator', null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='group members', through='groups.Membership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='wisegroup',
            field=models.ForeignKey(verbose_name='group', to='groups.WiseGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='wiseuser',
            field=models.ForeignKey(related_name=b'groups_membership_set', verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]