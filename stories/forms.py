from .models import Story
from django.forms import ModelForm
from django import forms


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'slug',
                  'status', 'story',
                  'caption'
                  ]
        widgets = {
            'slug': forms.HiddenInput,
        }

    def save(self, commit=True):
        storyimage = super().save(commit=False)
        if commit:
            storyimage.save()
        return storyimage
