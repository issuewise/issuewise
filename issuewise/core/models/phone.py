from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import StatusField
from django.utils.translation import ugettext_lazy as _


class PhoneNumberMixin(models.Model):

    PHONE_NUMBER_LABEL = (
        ('U', 'unknown'),
        ('M', 'mobile'),
        ('L', 'fixed-line'),
        )

    phone = PhoneNumberField(_('phone number'), null = True, blank = True)
    phone_label = StatusField(_('what kind of phone'), choices_name = 'PHONE_NUMBER_LABEL')
    is_primary_phone = models.BooleanField(_('is this the primary phone?'),
        default = False)

    class Meta:
        abstract = True


