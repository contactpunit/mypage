from django.urls import path, re_path
from .views import get_all_stories, story_detail, add_story, get_others_stories

app_name = 'stories'
urlpatterns = [
    # path('', get_all_stories, name='list_stories'),
    # path('newstory/', add_story, name='add_story'),
    path('<int:year>/<int:month>/<int:day>/<slug:story>/',
         story_detail,
         name='detail_story'),
    re_path(r'(?P<author>\d+)', get_others_stories, name='get_user_stories'),
]
