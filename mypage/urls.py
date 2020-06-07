from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stories/', include('stories.urls', namespace='stories')),
    path('account/', include('account.urls', namespace='account')),
]
