from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Subscribable(models.Model):
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
    subscriber=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('user'))
    subscribed_at=models.DateTimeField(_('time subscribed'), 
        auto_now_add=True)
    
    class Meta:
        abstract = True


class Creatable(models.Model):
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
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set', 
        verbose_name=_('creator'), null=True, on_delete=models.SET_NULL)
    created_at=models.DateTimeField(_('time created'), 
        auto_now_add=True)
    
    class Meta:
        abstract = True
