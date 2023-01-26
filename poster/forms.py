from django import forms
from .models import Poster


class PosterCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = Poster
        fields = [
            'image',
            'title',
            'description',
            'tags'
        ]
        widgets = {
            'image': forms.FileInput(attrs={
                'type': 'file',
                'name': 'image',
                'accept': 'image/*',
                'required id': 'id_image',
                'class': 'form-control'
            }),
        }
        labels = {
            'image': 'Choose the image for this poster',
            'title': 'Add title to this poster',
            'description': 'Add description to this poster',
            'tags': 'Add related tags to this poster'
        }