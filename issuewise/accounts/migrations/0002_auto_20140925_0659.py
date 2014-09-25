# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiseuser',
            name='degeneracy',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wiseuser',
            name='uri_name',
            field=models.TextField(null=True, verbose_name='encoded uri name', blank=True),
        ),
    ]
