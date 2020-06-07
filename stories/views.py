from django.shortcuts import render
from .models import Story


def get_all_stories(request):
    allstories = Story.objects.all()
    return render(request, 'stories/list_stories.html',
                  {'allstories': allstories})
