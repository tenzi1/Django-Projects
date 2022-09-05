from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_account/' ,views.CreateUserView.as_view(), name='create_user')
]
