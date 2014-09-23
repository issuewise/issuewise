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
            name='WiseLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=100, verbose_name='location name')),
                ('location_type', models.CharField(max_length=50, verbose_name='location type', choices=[(b'CO', b'Country'), (b'ST', b'State/Province'), (b'CI', b'City/Town/Village'), (b'GL', b'Global')])),
                ('creator', models.ForeignKey(related_name=b'locations_wiselocation_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name=b'children', verbose_name='parent', blank=True, to='locations.WiseLocation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
