# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('groupprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=300, verbose_name='social link')),
                ('website', models.CharField(max_length=3, verbose_name='name of website', choices=[(b'PER', b'Personal'), (b'ORG', b'Organization'), (b'FAC', b'Facebook'), (b'TWI', b'Twitter'), (b'GOO', b'Google'), (b'YOU', b'Youtube'), (b'SIN', b'Sina Weibo'), (b'QZO', b'Qzone'), (b'VIN', b'Vine'), (b'INS', b'Instagram'), (b'VK', b'VK'), (b'LIN', b'Linkedin'), (b'REN', b'Renren'), (b'PIN', b'Pinterest'), (b'TUM', b'Tumblr'), (b'FRI', b'Friendster'), (b'FOU', b'Foursquare'), (b'PAT', b'Path'), (b'MYS', b'Myspace'), (b'TUE', b'Tuenti'), (b'WOR', b'Wordpress'), (b'BLO', b'Blogger'), (b'SQU', b'Squarepage'), (b'MED', b'Medium'), (b'HUB', b'Hubpages'), (b'JUM', b'Jumla'), (b'LIV', b'Live Journal'), (b'QUO', b'Quora'), (b'TYP', b'Typepad'), (b'WEE', b'Weebly'), (b'DRU', b'Drupal'), (b'SQU', b'Squidoo'), (b'POS', b'Postachio'), (b'FBN', b'Facebook Notes'), (b'SVT', b'Svtle'), (b'SET', b'Sett'), (b'GHO', b'Ghost'), (b'PHA', b'Posthaven'), (b'PRS', b'Posterous'), (b'BLG', b'Blog'), (b'ZOO', b'Zoomshare'), (b'XAN', b'Xanga')])),
                ('link_type', models.CharField(max_length=3, verbose_name='this link goes to a', choices=[(b'SOC', b'social profile'), (b'BLO', b'blog'), (b'PER', b'personal website'), (b'ORG', b'organization website')])),
                ('autobiographer', models.ForeignKey(related_name=b'groupprofile_groupsociallink_set', verbose_name='group', to='groups.WiseGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='wisegroupprofile',
            name='group',
        ),
        migrations.AddField(
            model_name='wisegroupprofile',
            name='autobiographer',
            field=models.ForeignKey(related_name=b'groupprofile_wisegroupprofile_set', default=None, verbose_name='group', to='groups.WiseGroup'),
            preserve_default=False,
        ),
    ]
