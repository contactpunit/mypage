from django.urls import path
from .views import dashboard, get_all_artifacts

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='front'),
    path('<int:id>/<str:user>/artifacts/',
         get_all_artifacts,
         name='get_all_artifacts')
]

