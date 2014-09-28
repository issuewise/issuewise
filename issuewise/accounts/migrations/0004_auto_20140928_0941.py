# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usersociallink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='autobiographer',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='page',
        ),
        migrations.RemoveField(
            model_name='educationalinstitutions',
            name='autobiographer',
        ),
        migrations.RemoveField(
            model_name='educationalinstitutions',
            name='batch',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.RemoveField(
            model_name='educationalinstitutions',
            name='page',
        ),
        migrations.DeleteModel(
            name='EducationalInstitutions',
        ),
        migrations.RemoveField(
            model_name='usersociallink',
            name='autobiographer',
        ),
        migrations.DeleteModel(
            name='UserSocialLink',
        ),
        migrations.RemoveField(
            model_name='work',
            name='autobiographer',
        ),
        migrations.RemoveField(
            model_name='work',
            name='page',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
