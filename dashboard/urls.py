from django.urls import path
from .views import dashboard

app_name = 'account'

urlpatterns = [
    path('', dashboard, name='front'),
]
