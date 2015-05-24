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
        migrations.CreateModel(
            name='GroupSocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(help_text='url corresponding to a social link', max_length=300, verbose_name='social link')),
                ('website', models.CharField(help_text='the website corresponding         to the link. The backend automatically tries to identify the website         corresponding to the link and returns the identity of the website         as a three character code. When this identification fails, PER is         returned', max_length=3, verbose_name='name of website', choices=[(b'PER', b'Personal'), (b'ORG', b'Organization'), (b'FAC', b'Facebook'), (b'TWI', b'Twitter'), (b'GOO', b'Google'), (b'YOU', b'Youtube'), (b'SIN', b'Sina Weibo'), (b'QZO', b'Qzone'), (b'VIN', b'Vine'), (b'INS', b'Instagram'), (b'VK', b'VK'), (b'LIN', b'Linkedin'), (b'REN', b'Renren'), (b'PIN', b'Pinterest'), (b'TUM', b'Tumblr'), (b'FRI', b'Friendster'), (b'FOU', b'Foursquare'), (b'PAT', b'Path'), (b'MYS', b'Myspace'), (b'TUE', b'Tuenti'), (b'WOR', b'Wordpress'), (b'BLO', b'Blogger'), (b'SQU', b'Squarepage'), (b'MED', b'Medium'), (b'HUB', b'Hubpages'), (b'JUM', b'Jumla'), (b'LIV', b'Live Journal'), (b'QUO', b'Quora'), (b'TYP', b'Typepad'), (b'WEE', b'Weebly'), (b'DRU', b'Drupal'), (b'SQU', b'Squidoo'), (b'POS', b'Postachio'), (b'FBN', b'Facebook Notes'), (b'SVT', b'Svtle'), (b'SET', b'Sett'), (b'GHO', b'Ghost'), (b'PHA', b'Posthaven'), (b'PRS', b'Posterous'), (b'BLG', b'Blog'), (b'ZOO', b'Zoomshare'), (b'XAN', b'Xanga')])),
                ('link_type', models.CharField(help_text='denotes the type of social         link. SOC means Social Network, BLO means Blogs, PER means Personal         website and ORG means organizational website', max_length=3, verbose_name='this link goes to a', choices=[(b'SOC', b'social profile'), (b'BLO', b'blog'), (b'PER', b'personal website'), (b'ORG', b'organization website')])),
                ('autobiographer', models.ForeignKey(related_name=b'groupprofile_groupsociallink_set', verbose_name='group', to='groups.WiseGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WiseGroupProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_type', models.CharField(max_length=3, verbose_name='type of group', choices=[(b'MUS', b'Museums'), (b'ACA', b'Academic institutions'), (b'ADV', b'Advertising agencies'), (b'ANT', b'Antarctic agencies'), (b'BEA', b'Beauty organisations'), (b'CLU', b'Clubs and societies'), (b'COM', b'Committees'), (b'CMP', b'Companies'), (b'CRE', b'Credit rating agencies'), (b'CRI', b'Criminal organizations'), (b'DIA', b'Diaspora organizations'), (b'EMP', b'Employment agencies'), (b'EUG', b'Eugenics organizations'), (b'FAS', b'Fashion organizations'), (b'GLO', b'Globalization-related organizations'), (b'GOV', b'Government agencies'), (b'ILL', b'Illegal organizations'), (b'INT', b'International organizations'), (b'INV', b'Investment agencies'), (b'MIL', b'Military forces'), (b'MUS', b'Musical groups'), (b'NAT', b'National security institutions'), (b'NEW', b'News agencies'), (b'NPO', b'Non-profit organizations'), (b'PAR', b'Paramilitary organizations'), (b'PAY', b'Payment systems organizations'), (b'POL', b'Political organizations'), (b'PRO', b'Professional associations'), (b'RES', b'Research institutes'), (b'RST', b'Restaurants by type'), (b'SUP', b'Supraorganizations'), (b'TAL', b'Talent and literary agencies'), (b'TAX', b'Taxpayer groups'), (b'TOU', b'Tourism agencies'), (b'TRA', b'Training organizations'), (b'TRA', b'Travel agencies'), (b'OTH', b'Others')])),
                ('autobiographer', models.ForeignKey(related_name=b'groupprofile_wisegroupprofile_set', verbose_name='group', to='groups.WiseGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
