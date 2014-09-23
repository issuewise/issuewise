def creatable_factory(accounts_version_label, core_version_label):
    try:
        from accounts.models import creatable_factory as accounts_creatable_factory
        return accounts_creatable_factory(version_label = accounts_version_label)
    except:
        #pdb.set_trace()
        try:
            from core.utils import creatable_factory as core_creatable_factory
            return core_creatable_factory(version_label = core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.creatable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.creatable_factory' "
                       "is missing.") 
            raise ImportError(message)

def subscribable_factory(accounts_version_label, core_version_label):
    try:
        from accounts.models import subscribable_factory as accounts_subscribable_factory
        return accounts_subscribable_factory(version_label = accounts_version_label)
    except:
        try:
            from core.utils import subscribable_factory as core_subscribable_factory
            return core_subscribable_factory(version_label = core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.subscribable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.subscribable_factory' "
                       "is missing.") 
            raise ImportError(message)  

def owned_by_group_factory(version_label):
    """
    Factory method for the OwnedByGroup model. If you extend the
    OwnedByGroup model and want all your models to use the
    extended version, return it instead of OwnedByGroup

    Any extension of OwnedByGroup should extend from BaseOwnedByGroup,
    otherwise things will break
    """

    if version_label == 'latest':
        version_label = 'issuewise-1'
   
    if version_label == 'default-1':
        from groups.models.basemixins import BaseOwnedByGroup
        return BaseOwnedByGroup

    if version_label == 'issuewise-1':
        from groups.models.mixins import OwnedByWiseGroup
        return OwnedByWiseGroup

def group_hierarchy_factory(version_label):
    """
    Factory method for the GroupHierarchy model. If you extend the
    GroupHierarchy model and want all your models to use the
    extended version, return it instead of GroupHierarchy

    Any GroupHierarchy model should either extend from GroupHierarchy 
    or inherit Hierarchy, otherwise things will break
    """

    if version_label == 'latest':
        version_label = 'issuewise-1' 

    if version_label == 'issuewise-1':
        from groups.models.mixins import WiseGroupHierarchy
        return WiseGroupHierarchy
    
        
