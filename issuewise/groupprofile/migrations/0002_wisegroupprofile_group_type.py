# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisegroupprofile',
            name='group_type',
            field=models.CharField(default=None, max_length=3, verbose_name='type of group', choices=[(b'MUS', b'Museums'), (b'ACA', b'Academic institutions'), (b'ADV', b'Advertising agencies'), (b'ANT', b'Antarctic agencies'), (b'BEA', b'Beauty organisations'), (b'CLU', b'Clubs and societies'), (b'COM', b'Committees'), (b'CMP', b'Companies'), (b'CRE', b'Credit rating agencies'), (b'CRI', b'Criminal organizations'), (b'DIA', b'Diaspora organizations'), (b'EMP', b'Employment agencies'), (b'EUG', b'Eugenics organizations'), (b'FAS', b'Fashion organizations'), (b'GLO', b'Globalization-related organizations'), (b'GOV', b'Government agencies'), (b'ILL', b'Illegal organizations'), (b'INT', b'International organizations'), (b'INV', b'Investment agencies'), (b'MIL', b'Military forces'), (b'MUS', b'Musical groups'), (b'NAT', b'National security institutions'), (b'NEW', b'News agencies'), (b'NPO', b'Non-profit organizations'), (b'PAR', b'Paramilitary organizations'), (b'PAY', b'Payment systems organizations'), (b'POL', b'Political organizations'), (b'PRO', b'Professional associations'), (b'RES', b'Research institutes'), (b'RST', b'Restaurants by type'), (b'SUP', b'Supraorganizations'), (b'TAL', b'Talent and literary agencies'), (b'TAX', b'Taxpayer groups'), (b'TOU', b'Tourism agencies'), (b'TRA', b'Training organizations'), (b'TRA', b'Travel agencies'), (b'OTH', b'Others')]),
            preserve_default=False,
        ),
    ]
