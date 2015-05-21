# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('accounts', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='page',
            field=models.ForeignKey(related_name=b'accounts_work_set', verbose_name='page', blank=True, to='pages.WisePage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userfollowuser',
            name='followee',
            field=models.ForeignKey(related_name=b'accounts_userfollowuser_followee', verbose_name='followee', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userfollowuser',
            name='follower',
            field=models.ForeignKey(related_name=b'accounts_userfollowuser_follower', verbose_name='follower', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educationalinstitutions',
            name='autobiographer',
            field=models.ForeignKey(related_name=b'accounts_educationalinstitutions_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educationalinstitutions',
            name='batch',
            field=models.OneToOneField(related_name=b'academic institution', null=True, blank=True, to='accounts.Batch', verbose_name='class of'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educationalinstitutions',
            name='page',
            field=models.ForeignKey(related_name=b'accounts_educationalinstitutions_set', verbose_name='page', blank=True, to='pages.WisePage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batch',
            name='autobiographer',
            field=models.ForeignKey(related_name=b'accounts_batch_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batch',
            name='page',
            field=models.ForeignKey(related_name=b'accounts_batch_set', verbose_name='page', blank=True, to='pages.WisePage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wiseuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wiseuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
