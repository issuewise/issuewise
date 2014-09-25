# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20140925_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiseuser',
            name='activity_status',
            field=model_utils.fields.StatusField(default=b'I', max_length=100, no_check_for_status=True, choices=[(b'I', b'inactive'), (b'A', b'active')]),
        ),
        migrations.AlterField(
            model_name='wiseuser',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor=b'activity_status'),
        ),
    ]
