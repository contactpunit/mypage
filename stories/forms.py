from .models import Story
from django.forms import ModelForm


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'body']
