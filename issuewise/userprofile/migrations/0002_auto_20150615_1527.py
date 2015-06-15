# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersociallink',
            name='website',
        ),
        migrations.AlterField(
            model_name='usersociallink',
            name='link_type',
            field=models.CharField(help_text='denotes the type of social         link. fac means facebook, twi means twitter, blo means blog, quo means quora         lin means linkedin, wik means wikipedia', max_length=3, verbose_name='this link goes to', choices=[(b'fac', b'facebook'), (b'twi', b'twitter'), (b'quo', b'quora'), (b'wik', b'wikipedia'), (b'lin', b'linkedin'), (b'blo', b'blog')]),
        ),
    ]
