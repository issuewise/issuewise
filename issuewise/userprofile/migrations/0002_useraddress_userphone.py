# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_1', models.CharField(max_length=50, verbose_name='address line 1')),
                ('line_2', models.CharField(max_length=50, null=True, verbose_name='address line 2', blank=True)),
                ('line_3', models.CharField(max_length=50, null=True, verbose_name='address line 3', blank=True)),
                ('zipcode', models.CharField(max_length=15, verbose_name='postal code')),
                ('is_primary_address', models.BooleanField(default=False, verbose_name='is this the primary address?')),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_useraddress_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(related_name=b'userprofile_useraddress_set', verbose_name='belongs to location', to='locations.WiseLocation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='phone number', blank=True)),
                ('phone_label', model_utils.fields.StatusField(default=b'U', max_length=100, verbose_name='what kind of phone', no_check_for_status=True, choices=[(b'U', b'unknown'), (b'M', b'mobile'), (b'L', b'fixed-line')])),
                ('is_primary_phone', models.BooleanField(default=False, verbose_name='is this the primary phone?')),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_userphone_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
