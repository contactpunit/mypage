from django.shortcuts import render, get_object_or_404
from .models import Story
from .forms import CommentForm


def get_all_stories(request):
    allstories = Story.objects.all()
    return render(request, 'stories/list_stories.html',
                  {'allstories': allstories})


def story_detail(request, year, month, day, story):
    story = get_object_or_404(Story, slug=story,
                              status='draft',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            render(request, 'stories/detail_story.html',
                   {'story': story,
                    'form': form
                    })
    else:
        form = CommentForm()
    return render(request,
                  'stories/detail_story.html',
                  {'story': story,
                   'form': form})
