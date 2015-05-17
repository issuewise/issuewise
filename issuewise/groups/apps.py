from django.apps import AppConfig
 
 
class GroupsConfig(AppConfig):
    """ THE APP CONFIGURATION CLASS FOR THE GROUPS APP """
 
    name = 'groups'
    verbose_name = 'wise group'
 
    def ready(self):
 
        # import signal handlers
        import groups.signals.handlers
