from django.urls import path
from .views import dashboard, get_all_artifacts, \
    get_users_by_category, homepage, byusers, artifact_details

app_name = 'dashboard'

urlpatterns = [
    path('', homepage, name='front'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/byuser', byusers, name='user_dashboard'),
    path('dashboard/artifacts', artifact_details, name='artifact_details'),
    # path('<int:id>/<str:user>/artifacts/',
    #      get_all_artifacts,
    #      name='get_all_artifacts'),
    # path('<int:catgy>/<str:ctryname>/',
    #      get_users_by_category,
    #      name='get_users_by_category')
]
