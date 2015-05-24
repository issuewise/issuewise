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
        ('pages', '0001_initial'),
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
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_educationalinstitutions_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('batch', models.OneToOneField(related_name=b'academic institution', null=True, blank=True, to='userprofile.Batch', verbose_name='class of')),
                ('page', models.ForeignKey(related_name=b'userprofile_educationalinstitutions_set', verbose_name='page', blank=True, to='pages.WisePage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_1', models.CharField(max_length=50, verbose_name='address line 1')),
                ('line_2', models.CharField(max_length=50, null=True, verbose_name='address line 2', blank=True)),
                ('line_3', models.CharField(max_length=50, null=True, verbose_name='address line 3', blank=True)),
                ('zipcode', models.CharField(max_length=15, verbose_name='postal code')),
                ('is_primary_address', models.BooleanField(default=False, verbose_name='is this the primary address?')),
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
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
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_userphone_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(help_text='url corresponding to a social link', max_length=300, verbose_name='social link')),
                ('website', models.CharField(help_text='the website corresponding         to the link. The backend automatically tries to identify the website         corresponding to the link and returns the identity of the website         as a three character code. When this identification fails, PER is         returned', max_length=3, verbose_name='name of website', choices=[(b'PER', b'Personal'), (b'ORG', b'Organization'), (b'FAC', b'Facebook'), (b'TWI', b'Twitter'), (b'GOO', b'Google'), (b'YOU', b'Youtube'), (b'SIN', b'Sina Weibo'), (b'QZO', b'Qzone'), (b'VIN', b'Vine'), (b'INS', b'Instagram'), (b'VK', b'VK'), (b'LIN', b'Linkedin'), (b'REN', b'Renren'), (b'PIN', b'Pinterest'), (b'TUM', b'Tumblr'), (b'FRI', b'Friendster'), (b'FOU', b'Foursquare'), (b'PAT', b'Path'), (b'MYS', b'Myspace'), (b'TUE', b'Tuenti'), (b'WOR', b'Wordpress'), (b'BLO', b'Blogger'), (b'SQU', b'Squarepage'), (b'MED', b'Medium'), (b'HUB', b'Hubpages'), (b'JUM', b'Jumla'), (b'LIV', b'Live Journal'), (b'QUO', b'Quora'), (b'TYP', b'Typepad'), (b'WEE', b'Weebly'), (b'DRU', b'Drupal'), (b'SQU', b'Squidoo'), (b'POS', b'Postachio'), (b'FBN', b'Facebook Notes'), (b'SVT', b'Svtle'), (b'SET', b'Sett'), (b'GHO', b'Ghost'), (b'PHA', b'Posthaven'), (b'PRS', b'Posterous'), (b'BLG', b'Blog'), (b'ZOO', b'Zoomshare'), (b'XAN', b'Xanga')])),
                ('link_type', models.CharField(help_text='denotes the type of social         link. SOC means Social Network, BLO means Blogs, PER means Personal         website and ORG means organizational website', max_length=3, verbose_name='this link goes to a', choices=[(b'SOC', b'social profile'), (b'BLO', b'blog'), (b'PER', b'personal website'), (b'ORG', b'organization website')])),
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
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
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
                ('date_of_birth', models.DateField(help_text='Date of birth of the user expressed in the format     yyyy-mm-dd', null=True, verbose_name='born on', blank=True)),
                ('gender', models.CharField(help_text='Gender of the user. Can be any string         not exceeding 50 characters', max_length=50, null=True, verbose_name='gender', blank=True)),
                ('description', models.TextField(help_text='User bio. Can go on indefinitely', null=True, verbose_name='bio', blank=True)),
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
                ('privacy', models.CharField(help_text='Privacy of this entry.         Can be either A or F. A means public access. F means         friends only access', max_length=5, verbose_name='privacy settings', choices=[(b'A', b'all'), (b'F', b'friends only')])),
                ('designation', models.CharField(max_length=100, null=True, verbose_name='official position held by user', blank=True)),
                ('autobiographer', models.ForeignKey(related_name=b'userprofile_work_set', verbose_name='autobiographer', to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(related_name=b'userprofile_work_set', verbose_name='page', blank=True, to='pages.WisePage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
