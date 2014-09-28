# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wisegroupcategory',
            name='owner',
            field=models.ForeignKey(related_name=b'categories_wisegroupcategory_set', verbose_name='owner', to='groups.WiseGroup'),
        ),
    ]
