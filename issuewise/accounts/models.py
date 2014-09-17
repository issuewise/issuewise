import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from accounts.managers import WiseUserManager




class AbstractWiseUser(AbstractBaseUser, PermissionsMixin):
    """
    This is a copy of django.contrib.auth.AbstractUser with the 
	following changes :

	1. full_name and email_id are required and none
	of them are allowed to be Blank.

	2. email_id is used as the unique identifying field 

	3. url_name is the encoded version of full name which appears
       in the url for the user e.g issuewise.org/users/url_name

    4. uses a custom manager WiseUserManager which, among other things,
       sets the url_name from the full_name information.
    """
    url_name=models.TextField(_('encoded full name'))  
    full_name = models.CharField(_('full name'), max_length=200,
                 help_text=_('Required. 200 characters or fewer.'))
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = WiseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the full name for the user
        """
        return self.full_name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

		


class WiseUser(AbstractWiseUser):
    """
    This is the custom user model for Issuewise. Add any additional 
	fields in this model.
	
	Do not create new WiseUser instances using 
    WiseUser(full_name, email, **kwargs)! Instead use
	the safe manager methods WiseUser.objects.create_user(full_name, email, **kwargs)
    or WiseUser.objects.create_superuser(full_name, email, password, **kwargs)

    If you use ModelForm's save method to create and save the IWUser,
    you must assure the following before running save(commit=True):

	1. Trailing whitespaces in full_name must be stripped
    2. url_name should be set
    3. email must be normalized
    """
    class Meta(AbstractWiseUser.Meta):
        verbose_name = _('wise user')
        verbose_name_plural = _('wise users')



    
