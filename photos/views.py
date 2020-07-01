from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Photos
from .forms import PhotoForm
from catagories.models import Categories
from comments.forms import CommentForm


@login_required
def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(data=request.POST, files=request.FILES)
        current_category = Categories.objects.filter(category='Photos')
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.owner = request.user
            new_photo.categoryid = current_category[0]
            new_photo.save()
            return redirect(new_photo.get_absolute_url())
        else:
            form = PhotoForm()
    else:
        form = PhotoForm()
    return render(request, 'photos/add_photo.html',
                  {'form': form})


@login_required
def get_user_photos(request, owner=None):
    owner = owner if owner else request.user
    userphotos = Photos.objects.filter(owner=owner)
    page = request.GET.get('page', 1)
    paginator = Paginator(userphotos, 4)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request, 'photos/list_photos.html',
                  {'userphotos': userphotos,
                   'photos': photos})


@login_required
def photo_details(request, year, month, day, photo):
    pic = get_object_or_404(Photos,
                            slug=photo,
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
                   })


@login_required
@require_POST
def photo_like(request):
    pic_id = request.POST.get('id')
    action = request.POST.get('action')
    if pic_id and action:
        try:
            pic = Photos.objects.get(id=pic_id)
            if action == 'like':
                pic.users_like.add(request.user)
            else:
                pic.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})
