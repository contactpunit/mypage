from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photos
from comments.forms import CommentForm


@login_required
def get_user_photos(request):
    userphotos = Photos.objects.filter(owner=request.user)
    return render(request, 'photos/list_photos.html',
                  {'userphotos': userphotos})


@login_required
def photo_details(request, year, month, day, photo_slug):
    pic = get_object_or_404(Photos, slug=photo_slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    comments = pic.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content_object = pic
            new_comment.save()
    else:
        form = CommentForm()
    return render(request,
                  'photos/detail_photo.html',
                  {'pic': pic,
                   'comments': comments,
                   'form': form,
                   'new_comment': new_comment,
                   'year': year,
                   'month': month,
                   'day': day,
                   'photo_slug': photo_slug
                   })
