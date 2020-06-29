from django.urls import path, re_path
from .views import get_user_photos, photo_details, add_photo

app_name = 'photos'
urlpatterns = [
    path('', get_user_photos, name='list_photos'),
    path('addphoto', add_photo, name='add_photo'),
    path('photos/<int:year>/<int:month>/<int:day>/<slug:photo>/',
         photo_details,
         name='detail_photo'),
    re_path(r'(?P<owner>\d+)', get_user_photos, name='get_all_photos'),
]
