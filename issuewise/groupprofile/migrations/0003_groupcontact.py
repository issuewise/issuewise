# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groupprofile', '0002_auto_20140928_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='phone number', blank=True)),
                ('phone_label', model_utils.fields.StatusField(default=b'U', max_length=100, verbose_name='what kind of phone', no_check_for_status=True, choices=[(b'U', b'unknown'), (b'M', b'mobile'), (b'L', b'fixed-line')])),
                ('is_primary_phone', models.BooleanField(default=False, verbose_name='is this the primary phone?')),
                ('line_1', models.CharField(max_length=50, verbose_name='address line 1')),
                ('line_2', models.CharField(max_length=50, null=True, verbose_name='address line 2', blank=True)),
                ('line_3', models.CharField(max_length=50, null=True, verbose_name='address line 3', blank=True)),
                ('zipcode', models.CharField(max_length=15, verbose_name='postal code')),
                ('is_primary_address', models.BooleanField(default=False, verbose_name='is this the primary address?')),
                ('contact_person_is_user', models.BooleanField(default=False, verbose_name='is the contact personan Issuewise user?')),
                ('contact_person_name', models.CharField(max_length=200, null=True, verbose_name='name of the contact person', blank=True)),
                ('autobiographer', models.ForeignKey(related_name=b'groupprofile_groupcontact_set', verbose_name='group', to='groups.WiseGroup')),
                ('contact_person', models.ForeignKey(related_name=b'group_for_contact_person', verbose_name='contact person', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('location', models.ForeignKey(related_name=b'groupprofile_groupcontact_set', verbose_name='belongs to location', to='locations.WiseLocation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
