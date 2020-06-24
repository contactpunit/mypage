from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from stories.models import Story
from photos.models import Photos

app_name = 'dashboard'


# @login_required
# def dashboard(request):
#     other_users = User.objects.filter(~Q(username=request.user) & ~Q(is_superuser=True))
#     return render(request,
#                   'dashboard/dashboard.html',
#                   {'section': 'dashboard',
#                    'other_users': other_users})
@login_required
def dashboard(request):
    categories = ['stories']
    other_users = User.objects.filter(~Q(username=request.user) & ~Q(is_superuser=True))
    return render(request,
                  'dashboard/dashboard.html',
                  {'section': 'dashboard',
                   'other_users': other_users})


@login_required
def get_all_artifacts(request, id=None, user=None):
    stories = Story.objects.filter(author=id)
    # photos = Photos.objects.filter(author=user)
    return render(request,
                  'dashboard/userartifacts.html',
                  {'user': user,
                   'stories': stories,
                   'id': id
                   # 'photos': photos
                   })
