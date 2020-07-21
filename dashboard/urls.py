from django.urls import path
from .views import dashboard, get_all_artifacts, \
    get_users_by_category, byusers, user_all_photos, \
    user_all_stories, user_artifacts, upload_artifact, \
    get_all_users_stories, get_all_users_photos, homepage

app_name = 'dashboard'

urlpatterns = [
    path('', homepage, name='front'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/byuser', byusers, name='user_dashboard'),
    path('dashboard/allphotos', user_all_photos, name='user_all_photos'),
    path('dashboard/allstories', user_all_stories, name='user_all_stories'),
    path('dashboard/artifacts/<int:user>', user_artifacts, name='user_artifacts'),
    path('dashboard/upload', upload_artifact, name='upload_artifact'),
    path('dashboard/alluserstories', get_all_users_stories, name='get_all_users_stories'),
    path('dashboard/alluserphotos', get_all_users_photos, name='get_all_users_photos')
    # path('<int:id>/<str:user>/artifacts/',
    #      get_all_artifacts,
    #      name='get_all_artifacts'),
    # path('<int:catgy>/<str:ctryname>/',
    #      get_users_by_category,
    #      name='get_users_by_category')
]
