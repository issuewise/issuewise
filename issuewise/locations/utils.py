def creatable_factory(accounts_version_label, core_version_label):
    try:
        from accounts.models import creatable_factory as accounts_creatable_factory
        return accounts_creatable_factory(version_label = accounts_version_label)
    except:
        try:
            from core.utils import creatable_factory as core_creatable_factory
            return core_creatable_factory(version_label = core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.creatable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.creatable_factory' "
                       "is missing.") 
            raise ImportError(message)

def location_plug_factory(version_label):
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
        from locations.models.basemixins import BaseLocationPlug
        return BaseLocationPlug

def superlocation_plug_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'default-1'
    
    if version_label == 'default-1':
        from locations.models.basemixins import BaseSuperLocationPlug
        return BaseSuperLocationPlug

def address_plug_factory(version_label):
    
    if version_label == 'latest':
        version_label = 'default-1'
    
    if version_label == 'default-1':
        from locations.models.basemixins import BaseAddressPlug
        return BaseAddressPlug 
