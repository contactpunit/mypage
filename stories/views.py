from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.utils import IntegrityError
from .models import Story
from comments.forms import CommentForm
from stories.forms import StoryForm


@login_required
def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            pending_form = form.save(commit=False)
            pending_form.author = request.user
            pending_form.save()
            return redirect('stories:list_stories')
    else:
        form = StoryForm()
        return render(request,
                      'stories/add_story.html',
                      {'form': form})


@login_required
def get_all_stories(request):
    try:
        allstories = Story.objects.filter(author=request.user)
        page = request.GET.get('page', 1)
        paginator = Paginator(allstories, 4)
        try:
            stories = paginator.page(page)
        except PageNotAnInteger:
            stories = paginator.page(1)
        except EmptyPage:
            stories = paginator.page(paginator.num_pages)
        return render(request, 'stories/list_stories.html',
                      {'allstories': allstories,
                       'page': page,
                       'stories': stories})
    except IntegrityError:
        return HttpResponse("Error fetching stories")


@login_required
def story_detail(request, year, month, day, story):
    story = get_object_or_404(Story, slug=story,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    comments = story.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content_object = story
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
