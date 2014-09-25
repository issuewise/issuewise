from django.db import models
from django.utils.translation import ugettext_lazy as _
from userprofile.models.base import BaseUserProfile

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
)

class WiseUserProfile(BaseUserProfile):

    date_of_birth = models.DateTimeField(_('born on'))
    gender = models.CharField(_('gender'), max_length = 50,
        choices = GENDER_CHOICES)
    description = models.TextField(_('bio'))
    
    class Meta:
        abstract = True
        app_label = 'userprofile'
