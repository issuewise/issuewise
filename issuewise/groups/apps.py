from django.apps import AppConfig
 
 
class GroupsConfig(AppConfig):
 
    name = 'groups'
    verbose_name = 'Wise Group'
 
    def ready(self):
 
        # import signal handlers
        import groups.signals.handlers
