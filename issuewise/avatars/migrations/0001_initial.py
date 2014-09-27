# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import avatars.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiseAvatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=avatars.models.avatar_upload_path, max_length=300, verbose_name='avatar')),
                ('object_id', models.PositiveIntegerField(verbose_name='model primary key')),
                ('is_primary', models.BooleanField(default=True, verbose_name='is this the primary avatar?')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='uploaded at')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(max_length=300, null=True, upload_to=avatars.models.thumbnail_upload_path, blank=True)),
                ('content_type', models.ForeignKey(verbose_name='model type', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
