"""
This app's models are in multiple files inside a models
package instead of a single models.py file. This requires
some special treatment. 

Whenever you add new concrete models to this app, you need to

1. Import it here

2. Add your model class to __all__  

Please do this, otherwise Django will be confused when loading models,
might make errors in the schema declarations and even throw
unexpected errors! 
"""

from core.models.uri import UriNameMixin
from core.models.hierarchy import Hierarchy
from core.models.user import (UserAsFollower, UserAsCreator,
                              UserAsFollowee, UserAsMember,
                              UserAsAutobiographer)
from core.models.activity import ActivityMixin, LastModifiedMixin
from core.models.phone import PhoneNumberMixin
from core.models.sociallink import SocialLinkMixin

__all__ = ['UriNameMixin', 
           'Hierarchy', 
           'UserAsFollower',
           'UserAsCreator',
           'UserAsFollowee',
           'UserAsAutobiographer',
           'UserAsMember',
           'ActivityMixin', 
           'LastModifiedMixin',
           'PhoneNumberMixin',
           'SocialLinkMixin']
