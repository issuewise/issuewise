# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import avatars.models


class Migration(migrations.Migration):

    dependencies = [
        ('avatars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiseavatar',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(max_length=300, null=True, upload_to=avatars.models.thumbnail_upload_path, blank=True),
        ),
    ]
