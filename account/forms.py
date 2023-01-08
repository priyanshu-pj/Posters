from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None
        }


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = Profile
        fields = ['photo']