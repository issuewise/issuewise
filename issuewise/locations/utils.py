def user_as_creator_factory(accounts_version_label, core_version_label):
    try:
        from accounts.utils import user_as_creator_factory as accounts_user_as_creator_factory
        return accounts_user_as_creator_factory(accounts_version_label)
    except:
        try:
            from core.utils import user_as_creator_factory as core_user_as_creator_factory
            return core_user_as_creator_factory(core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.creatable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.creatable_factory' "
                       "is missing.") 
            raise ImportError(message)

def location_as_tag_factory(version_label):
    """
    Factory method for the LocationPlug model. If you extend the
    LocationPlug model and want all your models to use the
    extended version, return it instead of LocationPlug

    Any extension of LocationPlug should extend from BaseLocationPlug,
    otherwise things will break
    """
    if version_label == 'latest':
        version_label = 'default-1'
    
    if version_label == 'default-1':
        from locations.models.basemixins import LocationAsTag
        return LocationAsTag

def location_group_as_tag_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'default-1'
    
    if version_label == 'default-1':
        from locations.models.basemixins import LocationGroupAsTag
        return LocationGroupAsTag

def location_as_address_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'default-1'
    
    if version_label == 'default-1':
        from locations.models.basemixins import LocationAsAddress
        return LocationAsAddress
