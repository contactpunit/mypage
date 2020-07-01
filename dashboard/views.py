from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from stories.models import Story
from account.models import Profile
from photos.models import Photos
from catagories.models import Categories

app_name = 'dashboard'


def homepage(request):
    return render(request,
                  'dashboard/front.html')


@login_required
def dashboard(request):
    altimage = False
    altstories = False
    dashboard_pics = []
    dashboard_stories = []
    # ctgry = Categories.objects.all()
    stories = Story.objects.filter(author=request.user.id)
    pics = Photos.objects.filter(owner=request.user.id)
    if stories:
        if len(stories) >= 2:
            dashboard_stories = stories[:2]
        else:
            dashboard_stories = stories
    else:
        altstories = True
    if pics:
        if len(pics) >= 2:
            dashboard_pics = pics[:2]
        else:
            dashboard_pics = pics
    else:
        altimage = True
    return render(request,
                  'dashboard/dashboard.html',
                  {'section': 'dashboard',
                   'user': request.user,
                   'stories': stories,
                   'pics': pics,
                   'altimage': altimage,
                   'dashboard_pics': dashboard_pics,
                   'dashboard_stories': dashboard_stories,
                   'altstories': altstories
                   })


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


@login_required
def get_users_by_category(request, catgy=None, ctryname=None):
    other_users = User.objects.filter(~Q(username=request.user) & ~Q(is_superuser=True))
    return render(request,
                  'dashboard/get_users_by_ctrgy.html',
                  {'other_users': other_users,
                   'catgy': catgy,
                   'ctryname': ctryname
                   })


@login_required
def byusers(request):
    all_users = User.objects.filter(~Q(username=request.user) & ~Q(is_superuser=True))
    all_profiles = Profile.objects.all()
    profile_map = {user: profile
                   for user in all_users
                   for profile in all_profiles
                   if user.id == profile.user.id
                   }
    return render(request,
                  'dashboard/all_users.html',
                  {'profile_map': profile_map,
                   })


@login_required
def user_all_photos(request):
    pics = Photos.objects.filter(owner=request.user.id)
    return render(request,
                  'dashboard/storypainting.html',
                  {'pics': pics,
                   'ctry': 'photo'})


@login_required
def user_all_stories(request):
    stories = Story.objects.filter(owner=request.user.id)
    return render(request,
                  'dashboard/storypainting.html',
                  {'stories': stories,
                   'ctry': 'photo'})


@login_required
def user_artifacts(request, user):
    stories = Story.objects.filter(author=user)
    pics = Photos.objects.filter(owner=user)
    print(stories)
    print(pics)
    return render(request,
                  'dashboard/user_artifacts.html',
                  {'stories': stories,
                   'pics': pics})
