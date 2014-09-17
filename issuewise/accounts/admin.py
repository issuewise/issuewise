import re
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _


from accounts.models import WiseUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    error_messages = {
        'duplicate_username': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))


    class Meta:
        model = WiseUser
        fields = ('full_name', 'email')

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. 
        email = self.cleaned_data["email"]
        try:
            self.Meta.model.objects.get(email=email)
        except self.Meta.model.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        """
        Save the user after performing the following operations:

        1. Strip trailing whitespaces in full_name
        2. Normalize email
        3. Set the url_name field
        4. Set the hashed password
        """
        user = super(UserCreationForm, self).save(commit=False)
        user.full_name=re.sub(r"^\s+|\s+$","",user.full_name)
        user.url_name=self.Meta.model.objects.get_url_name(user.full_name)
        user.email=self.Meta.model.objects.normalize_email(user.email)
        user.set_password(self.cleaned_data["password1"])
		#user.set_url_name(self.Meta.objects.get_url_name(user.full_name))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = WiseUser
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class WiseUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name','url_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'password1', 'password2')}
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['email','full_name','url_name'] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []

# Now register the new UserAdmin...
admin.site.register(WiseUser, WiseUserAdmin)


