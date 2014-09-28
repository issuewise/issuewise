from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeFramedModel

from core.utils import (user_as_autobiographer_factory, social_link_factory,
                        phone_number_mixin_factory)
from pages.utils import page_as_reference_factory
from locations.utils import location_as_address_factory

UserAsAutobiographerClass = user_as_autobiographer_factory(version_label = 'latest')
SocialLinkClass = social_link_factory(version_label = 'latest')
PhoneNumberMixinClass = phone_number_mixin_factory(version_label = 'latest')
PageAsReferenceClass = page_as_reference_factory(version_label = 'latest')
LocationAsAddressClass = location_as_address_factory(version_label = 'latest')

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
)

class WiseUserProfile(UserAsAutobiographerClass):

    UserAsAutobiographerClass.autobiographer.unique = True

    date_of_birth = models.DateTimeField(_('born on'))
    gender = models.CharField(_('gender'), max_length = 50,
        choices = GENDER_CHOICES)
    description = models.TextField(_('bio'))
    
    class Meta:
        app_label = 'userprofile'


class EducationalInstitutions(UserAsAutobiographerClass, 
                              TimeFramedModel,
                              PageAsReferenceClass):

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
           PageAsReferenceClass):

    designation = models.CharField(_('official position held by user'),
        max_length = 100, null = True, blank = True)


    class Meta:
        app_label = 'userprofile'


class UserSocialLink(UserAsAutobiographerClass, SocialLinkClass):

   
    class Meta:
        app_label = 'userprofile'


class UserAddress(UserAsAutobiographerClass, LocationAsAddressClass):


    class Meta:
        app_label = 'userprofile'


class UserPhone(UserAsAutobiographerClass, PhoneNumberMixinClass):

    
    class Meta:
        app_label = 'userprofile'



