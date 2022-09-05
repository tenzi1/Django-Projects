
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include

urlpatterns = [
    path('password_change/',
         PasswordChangeView.as_view(template_name="password_change.html"),
         name='password_change'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dwitter.urls')),
    path('admin/', admin.site.urls),
    
]
