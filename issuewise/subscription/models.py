from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
	"""
	This is a plug for the WiseUser model. To establish any Many to Many
    relationship with the user and a model, inherit Subscription in the model.
	"""
	wiseuser=models.ForeignKey(settings.AUTH_USER_MODEL, 
                        related_name="%(app_label)s_%(class)s_set",
                        verbose_name=_("user"))
	subcribed_at=models.DateTimeField(_("time subscribed"), 
                                      auto_now_add=True)

	class Meta:
		abstract=True
