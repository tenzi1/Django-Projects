

from django.contrib import admin
from django.urls import include, re_path, path
from django.contrib.auth import views as auth_views
import users.views as user_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', user_views.home, name='home'),
#     path('register/', user_views.register,name='register'),
    
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/password_change', aupath_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change')
#     ]
urlpatterns = [
    
    re_path(r'admin/', admin.site.urls),
    path('password_change/', user_view.PasswordsChangeView.as_view(template_name='users/fake_password.html'), name='change-password'),
    path('password_success/', user_view.password_success, name='password_success'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name="users/fake_password.html"), name='password_change'),
    path('', include('users.urls')),
   
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password_form.html'),name='reset_password' ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]


