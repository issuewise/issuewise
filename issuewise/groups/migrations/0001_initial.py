# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(help_text='Required. 200 characters or less.', max_length=200, verbose_name='group name')),
                ('is_spokesgroup', models.BooleanField(default=False, verbose_name='represents the parent group')),
                ('creator', models.ForeignKey(related_name=b'groups_wisegroup_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name=b'children', verbose_name='parent', blank=True, to='groups.WiseGroup', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(related_name=b'members', verbose_name=b'group', to='groups.WiseGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='member',
            field=models.ForeignKey(related_name=b'groups_membership_set', verbose_name='member', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
