from django.conf.urls.static import static
from django.conf import settings
from account import views as user_view
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashbord.urls')),
    path('', include('account.urls')),
    path('register', user_view.register, name='registration-user'),
    path('profile', user_view.profile_user, name='profile-user'),
    path('profile/update/', user_view.profile_update, name='profile-update'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'),
          name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
          name='logout-user'),   

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='password-reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetView.as_view(template_name='user/password_reset_confirm.html'),
         name='password-reset-confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password-reset-complete'),


]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )

