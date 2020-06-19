from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photos


@login_required
def get_user_photos(request):
    userphotos = Photos.objects.filter(owner=request.user)
    return render(request, 'photos/list_photos.html',
                  {'userphotos': userphotos})


def photo_details(request, year, month, day, photo_slug):
    pic = get_object_or_404(Photos, slug=photo_slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request,
                  'photos/detail_photo.html',
                  {'pic': pic})
