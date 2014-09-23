from userprofile.models.base import BaseUserProfile

class WiseUserProfile(BaseUserProfile):
    
    class Meta:
        abstract = True
        app_label = 'userprofile'
