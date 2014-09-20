from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from core.models import uri_name_mixin_factory
from accounts.managers import BaseWiseUserManager, WiseUserManager

UriNameMixinClass = uri_name_mixin_factory()


class BaseWiseUser(AbstractBaseUser, PermissionsMixin):
    """
    ANY CUSTOM USER CLASS SHOULD INHERIT THIS MODEL

    Makes the following assumptions which should not be changed:

    1. Email is the unique identifying name for the user.

    2. User is either a superuser, or a staff or none. Superusers
    can log in and do almost anything that can be done using
    the admin interface. Staffs can log in to the admin interface
    and view all the data. Users who are neither staff nor 
    superusers cannot log in to the admin interface.

    3. Full name information is required to create an user. The full 
    name information is a singe field as naming
    conventions very across the world. The patterns First name, Last
    name or First Name, Middle Name, Last name are not universal.
    Given name, Other names is a good pattern, but Full name is 
    simpler.

    4. Users can join the website, either via registration or
    via the admin interface. This explains the attribute date_joined.

    5. Users can be members of canonical Django permission based 
    groups and can be given canonical Django permissions.

    6. Does NOT make any assumptions about characters allowed 
    in name or email.
    """  
    name = models.CharField(_('full name'), max_length=200,
        help_text=_('Required. 200 characters or fewer.'))
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    date_joined = models.DateTimeField(_('date joined'), 
        auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects=BaseWiseUserManager()

    class Meta:
        verbose_name = _('wise user')
        verbose_name_plural = _('wise users')
        abstract = True

    def get_full_name(self):
        """
        Returns the full name for the user
        """
        return self.name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class WiseUser(BaseWiseUser, UriNameMixinClass):
    """
    Issuewise users

    Assumptions that can change:

    1. Each user gets an correctly encoded uri_name which is a 
    part of the user URI e.g issuewise.org/users/url_name. This
    name is assigned the first time the WiseUser object gets saved.

    2. Full name has no trailing whitespaces

    3. Email is normalized

    4. The user account may be active or inactive. The account might
    be inactive for the following reasons:
        - email not verified
        - account deleted
        - account banned etc. 
    """
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    wise_user_manager=WiseUserManager()
    
    class Meta(BaseWiseUser.Meta):
        pass

    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = WiseUser.uri_name_manager.get_uri_name(self.name)
            self.email = WiseUser.objects.normalize_email(self.email)
        super(WiseUser,self).save(*args,**kwargs)



    
