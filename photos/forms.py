from django import forms
from .models import Photos


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('owner', 'title', 'slug',
                  'caption', 'publish', 'status',
                  'uploaded', 'updated', 'photo')
