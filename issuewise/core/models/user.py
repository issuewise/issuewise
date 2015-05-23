from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class UserAsFollower(models.Model):
    """
    THIS IS USED TO CREATE A SUBSCRIPTION LIKE RELATIONSHIP WITH
    THE USER MODEL

    Fields

    required : subscriber

        Denotes the subscriber (user). The subscription is deleted
        when the user gets deleted.

    auto : subscribed_at
        
        Denotes the time of subscription.

    Usage: 

        You have to do the following to make a model M subscribable:

        - Create a mixin model M' that has a ManyToManyField which
          points to settings.AUTH_USER_MODEL

        - If the many to many relation requires additional fields,
          then use "through" in the ManyToManyField to reference a
          custom join model

        - Inherit Subscribable in the "through" model using 
          subscribable_factory

        - Inherit the mixin model M' in the model M
    """
    follower=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_follower',
        verbose_name=_('follower'))
    folllowed_at=models.DateTimeField(_('time followed'), 
        auto_now_add=True, help_text = _('date and time at which the \
        relationship was initiated'))
    
    class Meta:
        abstract = True


class UserAsCreator(models.Model):
    """
    THIS IS USED TO CREATE A CREATOR LIKE RELATIONSHIP WITH
    THE USER MODEL.
    
    Field

    creator = NULL
        Denotes the creator (user). Set to NULL when the user is 
        deleted.
    
    auto : created_at
        Denotes the time of creation

    Usage:

        To make a model creatable, inherit this class in the model 
        that requires a creator using creatable_factory
    """
    
    def owner(self):
        return self.creator
    
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name =_('creator'), null=True, on_delete=models.SET_NULL)
    created_at=models.DateTimeField(_('time created'), 
        auto_now_add=True)

    
    class Meta:
        abstract = True


class UserAsAutobiographer(models.Model):
    
    autobiographer = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name =_('autobiographer'))
        
    def owner(self):
        return self.autobiographer

    
    class Meta:
        abstract = True


class UserAsFollowee(models.Model):

    followee = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = '%(app_label)s_%(class)s_followee', 
        verbose_name =_('followee'))

    
    class Meta:
        abstract = True


class UserAsMember(models.Model):

    member = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name =_('member'))

    
    class Meta:
        abstract = True


class UserAsModerator(models.Model):

    moderator = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name =_('moderator'))

    
    class Meta:
        abstract = True