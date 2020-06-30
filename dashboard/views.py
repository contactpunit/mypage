from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from stories.models import Story
from account.models import Profile
from catagories.models import Categories

app_name = 'dashboard'


def homepage(request):
    return render(request,
                  'dashboard/front.html')


@login_required
def dashboard(request):
    ctgry = Categories.objects.all()
    # other_users = User.objects.filter(~Q(username=request.user) & ~Q(is_superuser=True))
    return render(request,
                  'dashboard/dashboard.html',
                  {'section': 'dashboard',
                   'categories': ctgry})


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
    print(profile_map)
    return render(request,
                  'dashboard/all_users.html',
                  {'profile_map': profile_map,
                   })

