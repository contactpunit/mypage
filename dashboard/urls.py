from django.urls import path
from .views import dashboard, get_all_artifacts, \
    get_users_by_category, homepage, byusers, user_all_photos, \
    user_all_stories, user_artifacts

app_name = 'dashboard'

urlpatterns = [
    path('', homepage, name='front'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/byuser', byusers, name='user_dashboard'),
    path('dashboard/allphotos', user_all_photos, name='user_all_photos'),
    path('dashboard/allstories', user_all_stories, name='user_all_stories'),
    path('dashboard/artifacts/<int:user>', user_artifacts, name='user_artifacts')
    # path('<int:id>/<str:user>/artifacts/',
    #      get_all_artifacts,
    #      name='get_all_artifacts'),
    # path('<int:catgy>/<str:ctryname>/',
    #      get_users_by_category,
    #      name='get_users_by_category')
]
