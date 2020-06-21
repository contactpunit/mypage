from django.shortcuts import render
from django.contrib.auth.decorators import login_required

app_name = 'dashboard'


@login_required
def dashboard(request):
    return render(request,
                  'dashboard/dashboard.html',
                  {'section': 'dashboard'})
