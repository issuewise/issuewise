def creatable_factory(version_label):
    """
    Factory method for the Creatable model. If you extend the
    Creatable model and want all your models to use the
    extended version, return it instead of Creatable
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import Creatable
        return Creatable

def subscribable_factory(version_label):
    """
    Factory method for the Subscribable model. If you extend the
    Subscribable model and want all your models to use the
    extended version, return it instead of Subscribable
    """
    if version_label == 'latest':
        version_label = 'core-1'

    if version_label == 'core-1':
        from core.models.user import Subscribable
        return Subscribable

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


