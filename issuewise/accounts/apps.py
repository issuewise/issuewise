from django.apps import AppConfig
 
 
class AccountsConfig(AppConfig):
    """ THE APP CONFIGURATION CLASS FOR THE GROUPS APP """
 
    name = 'accounts'
    verbose_name = 'wise accounts'
 
    def ready(self):
 
        # import signal handlers
        import accounts.signals.handlers