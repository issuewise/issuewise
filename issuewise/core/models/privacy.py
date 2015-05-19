from django.db import models
from django.utils.translation import ugettext_lazy as _

PRIVACY_CHOICES = (
    ('A', 'all'),
    ('F', 'friends only'),
)

class PrivacyMixin(models.Model):

    privacy = models.CharField(_('privacy settings'), max_length=5,
        choices = PRIVACY_CHOICES)
        
    class Meta:
        abstract = True