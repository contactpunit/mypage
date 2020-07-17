from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from utils.utilities import generate_slug
from stories.models import Story
from account.models import Profile
from photos.models import Photos
from catagories.models import Categories
from photos.forms import PhotoForm
from stories.forms import StoryForm

app_name = 'dashboard'


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
                  'dashboard/viewmore.html',
                  {'pics': pics,
                   'ctry': 'photo'})


@login_required
def user_all_stories(request):
    stories = Story.objects.filter(author=request.user.id)
    return render(request,
                  'dashboard/viewmore.html',
                  {'stories': stories,
                   'ctry': 'story'})


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


@login_required
def upload_artifact(request):
    if request.method == 'POST':
        # doc = request.FILES
        # docname = doc['filepath']
        category = None
        artifacttype = request.POST.get('artifacttype', None)
        artifact = request.FILES.get('filepath', None)
        slug = generate_slug()
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['slug'] = slug
        request.POST['status'] = 'published'
        if artifacttype == 'P':
            category = 'Photos'
            request.FILES['photo'] = artifact
        elif artifacttype == 'S':
            category = 'Story'
            request.FILES['story'] = artifact
        request.POST._mutable = mutable
        result = helper(category, request)
        if result[0]:
            return redirect(result[1].get_absolute_url())
        else:
            return render(request, 'dashboard/upload.html')
    else:
        return render(request, 'dashboard/upload.html')


def helper(category, request):
    form = None
    result = False
    if category == 'Photos':
        form = PhotoForm(data=request.POST, files=request.FILES)
    elif category == 'Story':
        form = StoryForm(data=request.POST, files=request.FILES)
    current_category = Categories.objects.filter(category=category)
    if form.is_valid():
        if category == 'Photos':
            new_photo = form.save(commit=False)
            new_photo.owner = request.user
            new_photo.categoryid = current_category[0]
            new_photo.save()
            result = True
            return result, new_photo
        elif category == 'Story':
            pending_form = form.save(commit=False)
            pending_form.author = request.user
            pending_form.categoryid = current_category[0]
            pending_form.save()
            result = True
            return result, pending_form
        else:
            raise ValueError('category should be among predefined values')
    else:
        return result,
        # return render(request, 'dashboard/upload.html')
