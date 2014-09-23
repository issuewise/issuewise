# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WiseGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(help_text='Required. 200 characters or less.', max_length=200, verbose_name='group name')),
                ('creator', models.ForeignKey(related_name=b'groups_wisegroup_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True, verbose_name='time subscribed')),
                ('group', models.ForeignKey(related_name=b'groups_wisemembership_set', verbose_name='group', to='groups.WiseGroup')),
                ('subscriber', models.ForeignKey(related_name=b'groups_wisemembership_set', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wisegroup',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='group members', through='groups.WiseMembership'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wisegroup',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name=b'children', verbose_name='parent', blank=True, to='groups.WiseGroup', null=True),
            preserve_default=True,
        ),
    ]
