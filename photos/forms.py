from django import forms
from .models import Photos


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('title', 'slug',
                  'caption', 'status',
                  'photo')
        widgets = {
            'slug': forms.HiddenInput,
        }

    def save(self, commit=True):
        image = super().save(commit=False)
        if commit:
            image.save()
        return image
