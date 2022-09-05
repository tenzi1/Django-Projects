
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    # path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('application/', include('application.urls')),
    # path('', RedirectView.as_view(url='/application/', permanent=True))
]

# ONLY FOR DEVELOPMENT 
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL,
# document_root=settings.STATIC_ROOT)