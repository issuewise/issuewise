from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from issuewise.utils import get_model_from_settings

# get the user model and the group membership models as defined in
# settings

SiteGroupModel = get_model_from_settings(settings.SITE_GROUP_MODEL)
MembershipModel = get_model_from_settings(settings.GROUP_MEMBERSHIP_MODEL)

@receiver(post_save, sender = SiteGroupModel)
def member_on_create(sender, **kwargs):
    """
    When a group is created, makes the creator a member of the group
    """
    if kwargs.get('created', False):
        group = kwargs.get('instance')
        MembershipModel(group = group, subscriber = group.creator).save()
 
