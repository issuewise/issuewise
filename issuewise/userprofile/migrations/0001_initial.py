# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_batch_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(related_name=b'userprofile_batch_set', verbose_name='page', blank=True, to='pages.WisePage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationalInstitutions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_educationalinstitutions_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('batch', models.OneToOneField(related_name=b'academic institution', null=True, blank=True, to='userprofile.Batch', verbose_name='class of')),
                ('page', models.ForeignKey(related_name=b'userprofile_educationalinstitutions_set', verbose_name='page', blank=True, to='pages.WisePage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=300, verbose_name='social link')),
                ('website', models.CharField(max_length=3, verbose_name='name of website', choices=[(b'PER', b'Personal'), (b'ORG', b'Organization'), (b'FAC', b'Facebook'), (b'TWI', b'Twitter'), (b'GOO', b'Google'), (b'YOU', b'Youtube'), (b'SIN', b'Sina Weibo'), (b'QZO', b'Qzone'), (b'VIN', b'Vine'), (b'INS', b'Instagram'), (b'VK', b'VK'), (b'LIN', b'Linkedin'), (b'REN', b'Renren'), (b'PIN', b'Pinterest'), (b'TUM', b'Tumblr'), (b'FRI', b'Friendster'), (b'FOU', b'Foursquare'), (b'PAT', b'Path'), (b'MYS', b'Myspace'), (b'TUE', b'Tuenti'), (b'WOR', b'Wordpress'), (b'BLO', b'Blogger'), (b'SQU', b'Squarepage'), (b'MED', b'Medium'), (b'HUB', b'Hubpages'), (b'JUM', b'Jumla'), (b'LIV', b'Live Journal'), (b'QUO', b'Quora'), (b'TYP', b'Typepad'), (b'WEE', b'Weebly'), (b'DRU', b'Drupal'), (b'SQU', b'Squidoo'), (b'POS', b'Postachio'), (b'FBN', b'Facebook Notes'), (b'SVT', b'Svtle'), (b'SET', b'Sett'), (b'GHO', b'Ghost'), (b'PHA', b'Posthaven'), (b'PRS', b'Posterous'), (b'BLG', b'Blog'), (b'ZOO', b'Zoomshare'), (b'XAN', b'Xanga')])),
                ('link_type', models.CharField(max_length=3, verbose_name='this link goes to a', choices=[(b'SOC', b'social profile'), (b'BLO', b'blog'), (b'PER', b'personal website'), (b'ORG', b'organization website')])),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_usersociallink_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateTimeField(verbose_name='born on')),
                ('gender', models.CharField(max_length=50, verbose_name='gender', choices=[(b'M', b'male'), (b'F', b'female')])),
                ('description', models.TextField(verbose_name='bio')),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_wiseuserprofile_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(null=True, verbose_name='start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='end', blank=True)),
                ('page_status', models.BooleanField(default=False, verbose_name='any Issuewise page matching matching this entry?')),
                ('page_name', models.CharField(max_length=200, null=True, verbose_name='name of the person/group', blank=True)),
                ('description', models.TextField(null=True, verbose_name="description of the user's activities while at, and any continuing relations, with the user/group", blank=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='is the user currently involved with this user/group')),
                ('designation', models.CharField(max_length=100, null=True, verbose_name='official position held by user', blank=True)),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_work_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(related_name=b'userprofile_work_set', verbose_name='page', blank=True, to='pages.WisePage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
