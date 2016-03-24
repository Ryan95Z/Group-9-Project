from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from user.models import CamelUser


# creation form for creating users from terminal
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CamelUser
        fields = ()

    def clean_password_2(self):
        '''Check both passswords are clean and compare'''
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        '''Add new user to CAMEL'''
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
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
        model = CamelUser
        fields = ()

    def clean_password(self):
        '''Method to aquire original password'''
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    """Admin configuration for admin panel for viewing CAMEL user"""
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('get_short_name', 'first_name', 'last_name', 'email')
    list_filter = ('is_admin', 'is_an_lecturer', 'is_an_student',)
    fieldsets = (
        (None, {'fields': ('identifier', 'password', )}),
        ('Personal info', {'fields': ('identifier', 'first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_admin', 'is_an_student', 'is_an_lecturer',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('identifier', 'first_name', 'last_name', 'email', 'password1', 'password2')
                }),
    )
    search_fields = ('identifier',)
    ordering = ('identifier',)
    filter_horizontal = ()


admin.site.register(CamelUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)