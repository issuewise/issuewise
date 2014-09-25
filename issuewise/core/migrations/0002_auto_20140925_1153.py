# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phn',
            name='label',
            field=model_utils.fields.StatusField(default=b'U', max_length=100, verbose_name='what kind of phone', no_check_for_status=True, choices=[(0, 'dummy')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phn',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='phone number', blank=True),
        ),
    ]
