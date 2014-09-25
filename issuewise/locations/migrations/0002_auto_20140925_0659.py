# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiseSuperLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri_name', models.TextField(null=True, verbose_name='encoded uri name', blank=True)),
                ('degeneracy', models.PositiveIntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('name', models.CharField(max_length=200, verbose_name='superlocation name')),
                ('alliance_type', models.CharField(blank=True, max_length=60, null=True, verbose_name='alliance type', choices=[(b'CON', b'Continents'), (b'MIL', b'Military'), (b'ECO', b'Economic'), (b'HEA', b'Healthcare'), (b'ENV', b'Environmental'), (b'EDU', b'Educational'), (b'LAN', b'Language'), (b'PEA', b'Peace/Conflict Resolution'), (b'REG', b'Regional'), (b'CUL', b'Cultural'), (b'ETH', b'Ethnic'), (b'REL', b'Religious'), (b'HIS', b'Historical'), (b'AID', b'Humanitarian Aid'), (b'OTH', b'Others')])),
                ('creator', models.ForeignKey(related_name=b'locations_wisesuperlocation_set', on_delete=django.db.models.deletion.SET_NULL, verbose_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wiselocation',
            name='colloquial_location_type',
            field=models.CharField(default=None, max_length=50, verbose_name=b'colloquial location type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wiselocation',
            name='degeneracy',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wiselocation',
            name='location_type',
            field=models.CharField(max_length=50, verbose_name='offcial location type defined by geographic databases', choices=[(b'COU', b'Country'), (b'AD1', b'Primary administrative division'), (b'AD2', b'Secondary administrative division'), (b'AD3', b'Tertiary administrative division'), (b'CIT', b'Major populated region like cities/towns/villages'), (b'SUB', b'Suburban regions')]),
        ),
        migrations.AlterField(
            model_name='wiselocation',
            name='uri_name',
            field=models.TextField(null=True, verbose_name='encoded uri name', blank=True),
        ),
    ]
