import re
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.utils.http import urlquote

class IWUserManager(BaseUserManager):

	def get_url_name(self,full_name):
		"""
		Determines and returns an unique URI identifier for the given 
        full name. Separating whitespaces are stripped and replaced with "-". 
        Rest of the characters are encoded.

		Any trailing whitespaces at the beginning or end of full_name
        should be stripped before calling this function.
        """
		full_name=re.sub(r"\s+",'-',full_name)
		url_name=urlquote(full_name)
		count=self.filter(url_name=url_name).count()
		if count!=0:
			url_name=urlquote(full_name+u'-'+unicode(count))
		return url_name
		

	def _create_user(self, full_name, email, password,
                     is_staff, is_superuser, **extra_fields):
		"""
		Creates and saves a User with a url_name,
		full_name, email and password.

		Trailing whitespaces in full_name are stripped.

		Email is passed as is, because email will be verified.
		"""
		now = timezone.now()
		if not full_name:
			raise ValueError('The full name must be set')
		if not email:
			raise ValueError('The email must be set')
		full_name=re.sub(r"^\s+|\s+$","",full_name)
		url_name=self.get_url_name(full_name)
		email = self.normalize_email(email)
		user = self.model(url_name=url_name, full_name=full_name,
                          email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, full_name, email, 
                    password=None, **extra_fields):
		return self._create_user(full_name, email, password, 
                                 False, False, **extra_fields)

	def create_superuser(self, full_name, 
						 email, password, **extra_fields):
		return self._create_user(full_name, email, password, 
                                 True, True, **extra_fields)

