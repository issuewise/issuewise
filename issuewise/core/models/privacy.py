from django.db import models
from django.utils.translation import ugettext_lazy as _

PRIVACY_CHOICES = (
    ('A', 'all'),
    ('F', 'friends only'),
)

class PrivacyMixin(models.Model):

    privacy = models.CharField(_('privacy settings'), max_length=5,
        choices = PRIVACY_CHOICES, help_text = _('Privacy of this entry. \
        Can be either A or F. A means public access. F means \
        friends only access'))
        
    class Meta:
        abstract = True