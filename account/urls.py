from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from django.urls import reverse_lazy, include

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                              email_template_name='registration/password_reset_email.html',
                                              success_url='/password_reset/done/'), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register/', register, name='register'),
    path('edit/', profile, name='profile'),
    path('stories/', include('stories.urls', namespace='stories')),
    path('photos/', include('photos.urls', namespace='photos'))
]
