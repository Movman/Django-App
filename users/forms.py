from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from users.models import CustomUser


class CustomUserEditForm(UserEditForm):
    profile = forms.ModelChoiceField(queryset=CustomUser.objects, required=False, label=_("Profile"))


class CustomUserCreationForm(UserCreationForm):
    profile = forms.ModelChoiceField(queryset=CustomUser.objects, required=False, label=_("Profile"))