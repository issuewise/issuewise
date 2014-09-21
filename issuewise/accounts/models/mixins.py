from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def creatable_factory():
    """
    Factory method for the Creatable model. If you extend the
    Creatable model and want all your models to use the
    extended version, return it instead of Creatable

    Any extension of Creatable should extend from BaseCreatable,
    otherwise things will break
    """
    return Creatable

def subscribable_factory():
    """
    Factory method for the Subscribable model. If you extend the
    Subscribable model and want all your models to use the
    extended version, return it instead of Subscribable

    Any extension of Subscribable should extend from BaseSubscribable,
    otherwise things will break
    """
    return Subscribable


class BaseSubscribable(models.Model):
    """
    ANY CUSTOM SUBSCRIBABLE MODEL SHOULD INHERIT THIS MODEL
    SUBSCRIPTION IS A MANY TO MANY RELATIONSHIP

    Fields

    required : subscriber

        Denotes the subscriber (user). The subscription is deleted
        when the user gets deleted.

    auto : subscribed_at
        
        Denotes the time of subscription.

    Additional info: 

        You have to do the following to make a model M subscribable:

        - Create a mixin model M' that has a ManyToManyField which
          points to settings.AUTH_USER_MODEL.

        - If the many to many relation requires additional fields,
          then use "through" in the ManyToManyField to reference a
          custom join model.

        - Inherit Subscribable in the "through" model.

        - Inherit the mixin model M' in the model M.
    """
    subscriber=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('user'))
    subscribed_at=models.DateTimeField(_('time subscribed'), 
        auto_now_add=True)

    class Meta:
        abstract = True


class Subscribable(BaseSubscribable):
    """
    THIS IS USED TO CREATE A SUBSCRIPTION LIKE RELATIONSHIP WITH
    THE USER MODEL

    Fields

    required : subscriber

        see BaseSubscribable.subscriber

    auto : subscribed_at
        
        see BaseSubscribable.subscribed_at

    Additional info: 

        You have to do the following to make a model M subscribable:

        - Create a mixin model M' that has a ManyToManyField which
          points to settings.AUTH_USER_MODEL.

        - If the many to many relation requires additional fields,
          then use "through" in the ManyToManyField to reference a
          custom join model.

        - Inherit Subscribable in the "through" model.

        - Inherit the mixin model M' in the model M.
    """
    
    class Meta:
        abstract = True


class BaseCreatable(models.Model):
    """
    ANY CUSTOM CREATABLE MODEL SHOULD INHERIT FROM THIS MODEL
    CREATOR IS A ONE TO ONE RELATIONSHIP

    Field

    creator = NULL
        Denotes the creator (user). Set to NULL when the user is 
        deleted.
    
    auto : created_at
        Denotes the time of creation
    """
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set', 
        verbose_name=_('creator'), null=True, on_delete=models.SET_NULL)
    created_at=models.DateTimeField(_('time created'), 
        auto_now_add=True)

    class Meta:
        abstract=True


class Creatable(BaseCreatable):
    """
    THIS IS USED TO CREATE A CREATOR LIKE RELATIONSHIP WITH
    THE USER MODEL.
    
    creator = NULL
        see BaseCreatable.creator
    
    auto : created_at
        see BaseCreatable.created_at

    Additional info:

        To make a model creatable, inherit this class in the model 
        that requires a creator.
    """
    
    class Meta:
        abstract = True



