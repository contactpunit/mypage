from django.shortcuts import render, get_object_or_404
from .models import Story
from comments.forms import CommentForm


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
    comments = story.storycomments.filter(active=True)
    print(comments)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.story = story
            new_comment.save()
    else:
        form = CommentForm()
    return render(request,
                  'stories/detail_story.html',
                  {'story': story,
                   'comments': comments,
                   'form': form,
                   'new_comment': new_comment
                   })
