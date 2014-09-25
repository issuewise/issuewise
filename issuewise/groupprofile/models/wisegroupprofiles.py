from django.db import models
from django.utils.translation import ugettext_lazy as _

from groupprofile.models.base import BaseGroupProfile


class WiseGroupProfile(BaseGroupProfile):

    GROUP_TYPE_LIST = (
        ('MUS', 'Museums'), 
        ('ACA', 'Academic institutions'), 
        ('ADV', 'Advertising agencies'),
        ('ANT', 'Antarctic agencies'), 
        ('BEA', 'Beauty organisations'), 
        ('CLU', 'Clubs and societies'), 
        ('COM', 'Committees'),
        ('CMP', 'Companies'), 
        ('CRE', 'Credit rating agencies'),
        ('CRI', 'Criminal organizations'), 
        ('DIA', 'Diaspora organizations'),
        ('EMP', 'Employment agencies'),
        ('EUG', 'Eugenics organizations'),  
        ('FAS', 'Fashion organizations'), 
        ('GLO', 'Globalization-related organizations'), 
        ('GOV', 'Government agencies'), 
        ('ILL', 'Illegal organizations'), 
        ('INT', 'International organizations'), 
        ('INV', 'Investment agencies'),  
        ('MIL', 'Military forces'), 
        ('MUS', 'Musical groups'),
        ('NAT', 'National security institutions'), 
        ('NEW', 'News agencies'), 
        ('NPO', 'Non-profit organizations'), 
        ('PAR', 'Paramilitary organizations'), 
        ('PAY', 'Payment systems organizations'), 
        ('POL', 'Political organizations'), 
        ('PRO', 'Professional associations'), 
        ('RES', 'Research institutes'), 
        ('RST', 'Restaurants by type'),
        ('SUP', 'Supraorganizations'),
        ('TAL', 'Talent and literary agencies'), 
        ('TAX', 'Taxpayer groups'),
        ('TOU', 'Tourism agencies'),
        ('TRA', 'Training organizations'), 
        ('TRA', 'Travel agencies'),
        ('OTH', 'Others'),
) 

    group_type = models.CharField(_('type of group'),
            max_length = 3, choices = GROUP_TYPE_LIST)
    
    class Meta:
        app_label = 'groupprofile'
