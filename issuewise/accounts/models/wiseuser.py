from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from core.models import uri_name_mixin_factory
from accounts.managers import BaseWiseUserManager, WiseUserManager

# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory()


class BaseWiseUser(AbstractBaseUser, PermissionsMixin):
    """
    ANY CUSTOM USER CLASS SHOULD INHERIT THIS MODEL

    Fields

    Required: email

        Email is the unique identifying name for the user. No 
        assumptions about characters allowed in email. 
        Everything is allowed.

    is_superuser = False , is_staff = False

        User is either a superuser, or a staff or none. Superusers
        can log in and do almost anything that can be done using
        the admin interface. Staffs can log in to the admin interface
        and view all the data. Users who are neither staff nor 
        superusers cannot log in to the admin interface.

    Required : name
        
        Full name of an user. No assumptions about characters allowed 
        in email. Everything is allowed.
        The full name information is a single field as naming 
        conventions very across the world. The patterns First name, 
        Lastname or First Name, Middle Name, Last name are not 
        universal. Given name, Other names is a good pattern, but 
        Full name is simpler.

    auto : date_joined
    
        Users can join the website, either via registration or
        via the admin interface. The time of joing is stored
        automatically in date_joined.

    Additional information:
        
        Fully compatible with django authorization.
        Users can be members of canonical Django permission based 
        groups and can be given canonical Django permissions.
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
    ISSUEWISE USERS

    Fields

    auto : uri_name

        Each user gets a correctly encoded uri_name. The uri_name
        appears in the user URI as shown below:
        issuewise.org/users/wiseuser_uri_name
        This name is automatically assigned when the WiseUser object 
        is saved to the database for the first time.

    required : name

        see BaseWiseUser.name 
        All trailing whitespaces are removed when the WiseUser object 
        is saved to the database for the first time.

    required : email
        
        see BaseWiseUser.email
        Email is normalized when the WiseUser object 
        is saved to the database for the first time.

    is_active = False

        Denotes whether the user account is active or inactive. 
        The account might be inactive for the following reasons:
        - email not verified
        - account deleted
        - account banned etc. 
    """
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    wise_user_manager=WiseUserManager()
    
    class Meta(BaseWiseUser.Meta):
        app_label = 'accounts'

    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field,
        populates the uri_name field based on the cleaned name and
        normalizes email.
        """
        if not self.id:
            self.clean_name()
            self.uri_name = WiseUser.uri_name_manager.get_uri_name(self.name)
            self.email = WiseUser.objects.normalize_email(self.email)
        super(WiseUser,self).save(*args,**kwargs)



    
