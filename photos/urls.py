from django.urls import path
from .views import get_user_photos, photo_details, add_photo

app_name = 'photos'
urlpatterns = [
    path('', get_user_photos, name='list_photos'),
    path('addphoto', add_photo, name='add_photo'),
    path('photos/<int:year>/<int:month>/<int:day>',
         photo_details,
         name='detail_photo'),
]
