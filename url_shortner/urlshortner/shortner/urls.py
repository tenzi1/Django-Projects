from django.urls import path
from . import views

appname = "shortner" #declares namespacing of this app
urlpatterns = [
    path('', views.home_view, name='home' ),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect'),
]