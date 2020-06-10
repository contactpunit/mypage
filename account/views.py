from django.shortcuts import render
from .models import Profile
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,
                  'registration/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
        else:
            return render(request,
                          'registration/register.html',
                          {'user_form': user_form})

    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'registration/register.html',
                      {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        userform = UserForm(instance=request.user,
                            data=request.POST)
        profileform = ProfileForm(instance=request.user.profile,
                                  data=request.POST,
                                  files=request.FILES)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return render(request, 'registration/profile_saved.html')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/edit.html',
                  {'userform': userform,
                   'profileform': profileform})
