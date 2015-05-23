from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeFramedModel

from core.utils import (user_as_autobiographer_factory, social_link_factory,
                        phone_number_mixin_factory, privacy_mixin_factory)
from pages.utils import page_as_reference_factory
from locations.utils import location_as_address_factory

UserAsAutobiographerClass = user_as_autobiographer_factory(version_label = 'latest')
SocialLinkClass = social_link_factory(version_label = 'latest')
PhoneNumberMixinClass = phone_number_mixin_factory(version_label = 'latest')
PageAsReferenceClass = page_as_reference_factory(version_label = 'latest')
LocationAsAddressClass = location_as_address_factory(version_label = 'latest')
PrivacyMixinClass = privacy_mixin_factory(version_label = 'latest')


class WiseUserProfile(UserAsAutobiographerClass, PrivacyMixinClass):

    UserAsAutobiographerClass.autobiographer.unique = True

    date_of_birth = models.DateField(_('born on'), null = True, blank = True,
    help_text = _('Date of birth of the user expressed in the format \
    yyyy-mm-dd'))
    gender = models.CharField(_('gender'), max_length = 50, null = True, 
        blank = True, help_text = _('Gender of the user. Can be any string \
        not exceeding 50 characters'))
    description = models.TextField(_('bio'), null = True, blank = True,
        help_text = _('User bio. Can go on indefinitely'))
    
        
    #def _str_(self):
    #    return self.autobiographer.name
    
    class Meta:
        app_label = 'userprofile'


class EducationalInstitutions(UserAsAutobiographerClass, 
                              TimeFramedModel,
                              PageAsReferenceClass,
                              PrivacyMixinClass):

    batch = models.OneToOneField(settings.BATCH_MODEL,
        related_name = 'academic institution', 
        verbose_name = _('class of'),
        null = True, blank = True)

    class Meta:
        app_label = 'userprofile'


class Batch(UserAsAutobiographerClass, PageAsReferenceClass):

    class Meta:
        app_label = 'userprofile'


class Work(UserAsAutobiographerClass, 
           TimeFramedModel,
           PageAsReferenceClass,
           PrivacyMixinClass):

    designation = models.CharField(_('official position held by user'),
        max_length = 100, null = True, blank = True)


    class Meta:
        app_label = 'userprofile'


class UserSocialLink(UserAsAutobiographerClass, SocialLinkClass, PrivacyMixinClass):

    def save(self,*args,**kwargs):
        self.link_type = self.get_website_type()
        super(UserSocialLink,self).save(*args,**kwargs)
   
    class Meta:
        app_label = 'userprofile'


class UserAddress(UserAsAutobiographerClass, LocationAsAddressClass, PrivacyMixinClass):


    class Meta:
        app_label = 'userprofile'


class UserPhone(UserAsAutobiographerClass, PhoneNumberMixinClass, PrivacyMixinClass):

    
    class Meta:
        app_label = 'userprofile'


