from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from users.models import AuthorProfile
from polls.models import Question, Choice

class CustomUserEditForm(UserEditForm):
    profile = forms.ModelChoiceField(queryset=AuthorProfile.objects, required=False, label=_("Profile"))
    polls = forms.ModelChoiceField(queryset=Question.objects, required=False, label=_("Question"))
    choice = forms.ModelChoiceField(queryset=Choice.objects, required=False, label=_("Choice"))


class CustomUserCreationForm(UserCreationForm):
    profile = forms.ModelChoiceField(queryset=AuthorProfile.objects, required=False, label=_("Profile"))
    polls = forms.ModelChoiceField(queryset=Question.objects, required=False, label=_("Question"))
    choice = forms.ModelChoiceField(queryset=Choice.objects, required=False, label=_("Choice"))