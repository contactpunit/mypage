from django.urls import path
from .views import get_all_stories

app_name = 'stories'
urlpatterns = [
    path('', get_all_stories, name='list_stories'),
]
