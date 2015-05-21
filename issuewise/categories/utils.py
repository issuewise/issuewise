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

def public_category_as_tag_factory(version_label):
    """
    Factory method for the PublicCategoryPlug model. If you extend the
    PublicCategoryPlug model and want all your models to use the
    extended version, return it instead of PublicCategoryPlug

    Any extension of PublicCategoryPlug should extend from 
    BasePublicCategoryPlug, otherwise things will break
    """
    if version_label == 'latest':
        version_label = 'default-1'

    if version_label == 'default-1':
        from categories.models.mixins import PublicCategoryAsTag
        return PublicCategoryAsTag

def group_category_as_tag_factory(version_label):
    """
    Factory method for the GroupCategoryPlug model. If you extend the
    GroupCategoryPlug model and want all your models to use the
    extended version, return it instead of GroupCategoryPlug

    Any extension of GroupCategoryPlug should extend from 
    BaseGroupCategoryPlug, otherwise things will break
    """
    if version_label == 'latest':
        version_label = 'default-1'

    if version_label == 'default-1':
        from categories.models.basemixins import GroupCategoryAsTag
        return GroupCategoryAsTag
