from django import forms
from .models import Poster


class PosterCreationForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = "__all__"