from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Subscribable(models.Model):
    """
    This is a plug for the WiseUser model used for subscription
    like relationships. 

    Assumptions:

    1. Subscription is a many to many relation

    If the above assumption is true, do the following to make
    a model M subscribable.

    1. Create a mixin model M' that has a ManyToManyField which
    points to settings.AUTH_USER_MODEL.

    2. If the many to many relation requires additional fields,
    then use "through" in the ManyToManyField to reference a
    custom join model.

    3. Inherit Subscribable in the "through" model.

    4. Inherit the mixin model M' in the model M.
    """
    subscriber=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('user'))
    subscribed_at=models.DateTimeField(_('time subscribed'), 
        auto_now_add=True)

    class Meta:
        abstract=True


class Creatable(models.Model):
    """
    This is a plug for the WiseUser model for creator like
    relationships.

    Assumptions:

    1. Any object has one and only one creator.

    If this assumption is true, inherit this class in the model 
    that requires a creator.
    """
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='%(app_label)s_%(class)s_set', 
        verbose_name=_('creator'), null=True, on_delete=models.SET_NULL)
    created_at=models.DateTimeField(_('time created'), 
        auto_now_add=True)

    class Meta:
        abstract=True



