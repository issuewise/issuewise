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

def user_as_member_factory(accounts_version_label, core_version_label):
    try:
        from accounts.utils import user_as_member_factory as accounts_user_as_member_factory
        return accounts_user_as_member_factory(accounts_version_label)
    except:
        try:
            from core.utils import user_as_member_factory as core_user_as_member_factory
            return core_user_as_member_factory(core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.creatable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.creatable_factory' "
                       "is missing.") 
            raise ImportError(message)

def group_as_owner_factory(version_label):
    """
    Factory method for the OwnedByGroup model. If you extend the
    OwnedByGroup model and want all your models to use the
    extended version, return it instead of OwnedByGroup

    Any extension of OwnedByGroup should extend from BaseOwnedByGroup,
    otherwise things will break
    """

    if version_label == 'latest':
        version_label = 'default-1'
   
    if version_label == 'default-1':
        from groups.models.basemixins import GroupAsOwner
        return GroupAsOwner

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
    
        
