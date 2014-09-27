def user_as_creator_factory(version_label):
    """
    Factory method for the Creatable model. If you extend the
    Creatable model and want all your models to use the
    extended version, return it instead of Creatable
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import UserAsCreator
        return UserAsCreator

def user_as_follower_factory(version_label):
    """
    Factory method for the Subscribable model. If you extend the
    Subscribable model and want all your models to use the
    extended version, return it instead of Subscribable
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import UserAsFollower
        return UserAsFollower

def user_as_followee_factory(version_label):
    """
    Factory method for the Subscribable model. If you extend the
    Subscribable model and want all your models to use the
    extended version, return it instead of Subscribable
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import UserAsFollowee
        return UserAsFollowee

def user_as_autobiographer_factory(version_label):

    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import UserAsAutobiographer
        return UserAsAutobiographer

def user_as_member_factory(version_label):

    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import UserAsMember
        return UserAsMember


def uri_name_mixin_factory(version_label):
    """
    Factory method for the UriNameMixin model. If you extend the
    UriNameMixin model and want all your models to use the
    extended version, return it instead of UriNameMixin
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.uri import UriNameMixin
        return UriNameMixin

def hierarchy_factory(version_label):
    """
    Factory method for the Hierarchy model. If you extend the
    Hierarchy model and want all your models to use the
    extended version, return it instead of Hierarchy
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.hierarchy import Hierarchy
        return Hierarchy

def activity_mixin_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.activity import ActivityMixin
        return ActivityMixin

def phone_number_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.phone import PhoneNumberMixin
        return PhoneNumberMixin

def social_link_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.sociallink import SocialLinkMixin
        return SocialLinkMixin


