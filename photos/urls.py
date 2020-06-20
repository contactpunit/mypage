from django.urls import path
from .views import get_user_photos, photo_details

app_name = 'photos'
urlpatterns = [
    path('', get_user_photos, name='list_photos'),
    path('photos/<int:year>/<int:month>/<int:day>/<slug:photo_slug>',
         photo_details,
         name='detail_photo'),
]
