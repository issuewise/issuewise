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
            name='LocationGroupMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=100, verbose_name='location name')),
                ('location_type', models.CharField(max_length=50, verbose_name='offcial location type defined by geographic databases', choices=[(b'COU', b'Country'), (b'AD1', b'Primary administrative division'), (b'AD2', b'Secondary administrative division'), (b'AD3', b'Tertiary administrative division'), (b'CIT', b'Major populated region like cities/towns/villages'), (b'SUB', b'Suburban regions')])),
                ('colloquial_location_type', models.CharField(max_length=50, verbose_name=b'colloquial location type')),
                ('creator', models.ForeignKey(related_name=b'locations_wiselocation_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name=b'children', verbose_name='parent', blank=True, to='locations.WiseLocation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseLocationGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=200, verbose_name='location group name')),
                ('alliance_type', models.CharField(blank=True, max_length=60, null=True, verbose_name='alliance type', choices=[(b'CON', b'Continents'), (b'MIL', b'Military'), (b'ECO', b'Economic'), (b'HEA', b'Healthcare'), (b'ENV', b'Environmental'), (b'EDU', b'Educational'), (b'LAN', b'Language'), (b'PEA', b'Peace/Conflict Resolution'), (b'REG', b'Regional'), (b'CUL', b'Cultural'), (b'ETH', b'Ethnic'), (b'REL', b'Religious'), (b'HIS', b'Historical'), (b'AID', b'Humanitarian Aid'), (b'OTH', b'Others')])),
                ('creator', models.ForeignKey(related_name=b'locations_wiselocationgroup_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='locationgroupmembership',
            name='location_group',
            field=models.ForeignKey(related_name=b'members', verbose_name='location group', to='locations.WiseLocationGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationgroupmembership',
            name='member',
            field=models.ForeignKey(related_name=b'location_group', verbose_name='member locations', to='locations.WiseLocation'),
            preserve_default=True,
        ),
    ]
