import re
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class BaseWiseUserManager(BaseUserManager):


    def _create_user(self, name, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with a url_name,
        name, email and password.
        """
        now=timezone.now()
        if not name:
            raise ValueError('The full name must be set')
        if not email:
            raise ValueError('The email must be set')
        user = self.model(name=name,
                          email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, 
                    password=None, **extra_fields):
        return self._create_user(name, email, password, 
                                 False, False, **extra_fields)

    def create_superuser(self, name, 
                         email, password, **extra_fields):
        return self._create_user(name, email, password, 
                                 True, True, **extra_fields)


class WiseUserManager(BaseWiseUserManager):
    pass
    

