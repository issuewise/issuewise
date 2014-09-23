def creatable_factory(accounts_version_label, core_version_label):
    try:
        from accounts.models import creatable_factory as accounts_creatable_factory
        return accounts_creatable_factory(accounts_version_label)
    except:
        try:
            from core.utils import creatable_factory as core_creatable_factory
            return core_creatable_factory(core_version_label)
        except:
            message = ("Unsatisfied requirements for the 'groups' app. Requires "
                       "'core.models.creatable_factory'. Either the 'core' app "
                       "has not been installed or 'core.models.creatable_factory' "
                       "is missing.") 
            raise ImportError(message)

def public_category_plug_factory(version_label):
    """
    Factory method for the PublicCategoryPlug model. If you extend the
    PublicCategoryPlug model and want all your models to use the
    extended version, return it instead of PublicCategoryPlug

    Any extension of PublicCategoryPlug should extend from 
    BasePublicCategoryPlug, otherwise things will break
    """
    if version_label == 'latest':
        version_label = 'issuewise-1'

    if version_label == 'default-1':
        from categories.models.basemixins import BasePublicCategoryPlug
        return BasePublicCategoryPlug

    if version_label == 'issuewise-1':
        from categories.models.mixins import WisePublicCategoryPlug
        return WisePublicCategoryPlug

def group_category_plug_factory(version_label):
    """
    Factory method for the GroupCategoryPlug model. If you extend the
    GroupCategoryPlug model and want all your models to use the
    extended version, return it instead of GroupCategoryPlug

    Any extension of GroupCategoryPlug should extend from 
    BaseGroupCategoryPlug, otherwise things will break
    """
    if version_label == 'latest':
        version_label = 'issuewise-1'

    if version_label == 'default-1':
        from categories.models.basemixins import BaseGroupCategoryPlug
        return BaseGroupCategoryPlug

    if version_label == 'issuewise-1':
        from categories.models.mixins import WiseGroupCategoryPlug
        return WiseGroupCategoryPlug
