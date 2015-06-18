# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150617_2035'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wisefriendship',
            unique_together=set([('follower', 'followee')]),
        ),
    ]
