from django.urls import path
from . import views
urlpatterns = [
    path('publishers/', views.PublisherListView.as_view(), name="publisher")
]
  