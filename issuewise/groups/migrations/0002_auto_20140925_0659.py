# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisegroup',
            name='is_spokesgroup',
            field=models.BooleanField(default=False, verbose_name='represents the parent group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wisegroup',
            name='degeneracy',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wisegroup',
            name='uri_name',
            field=models.TextField(null=True, verbose_name='encoded uri name', blank=True),
        ),
    ]
