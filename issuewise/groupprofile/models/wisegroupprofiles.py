from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from core.utils import social_link_factory, phone_number_mixin_factory
from groups.utils import group_as_autobiographer_factory
from locations.utils import location_as_address_factory

SocialLinkClass = social_link_factory(version_label = 'latest')
PhoneNumberMixinClass = phone_number_mixin_factory(version_label = 'latest')
GroupAsAutobiographerClass = group_as_autobiographer_factory(version_label = 'latest')
LocationAsAddressClass = location_as_address_factory(version_label = 'latest')

class WiseGroupProfile(GroupAsAutobiographerClass):

    GroupAsAutobiographerClass.autobiographer.unique = True

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


class GroupSocialLink(GroupAsAutobiographerClass, SocialLinkClass):

    
    class Meta:
        app_label = 'groupprofile'


class GroupContact(GroupAsAutobiographerClass, PhoneNumberMixinClass,
                   LocationAsAddressClass):

    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = 'group_for_contact_person',
        verbose_name = _('contact person'), null = True, blank = True)

    contact_person_is_user = models.BooleanField(_('is the contact person'
        'an Issuewise user?'), default = False, blank = True)

    contact_person_name = models.CharField(_('name of the contact person'),
        max_length = 200, null = True, blank = True)

    
    class Meta:
        app_label = 'groupprofile'
    
