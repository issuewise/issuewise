from django.db import models
from model_utils.models import StatusField, MonitorField


class ActivityMixin(models.Model):

    activity_status = StatusField(choices_name = 'ACTIVITY_STATUS')
    explanation = StatusField(choices_name = 'ACTIVITY_STATUS_EXPLANATION')
    status_changed = MonitorField(monitor = 'activity_status')

    class Meta:
        abstract = True


class LastModifiedMixin(models.Model):

    last_modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
