# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20140925_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wiseuser',
            name='is_active',
        ),
        migrations.AddField(
            model_name='wiseuser',
            name='activity_status',
            field=model_utils.fields.StatusField(default=b'A', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wiseuser',
            name='explanation',
            field=model_utils.fields.StatusField(default=b'NV', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wiseuser',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor=b'status'),
            preserve_default=True,
        ),
    ]
