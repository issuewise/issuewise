def page_as_reference_factory(version_label):
    """
    Factory method for the Subscribable model. If you extend the
    Subscribable model and want all your models to use the
    extended version, return it instead of Subscribable
    """
    if version_label == 'latest':
        version_label = 'default-1'

    if version_label == 'default-1':
        from pages.models.basemixins import PageAsReference
        return PageAsReference
