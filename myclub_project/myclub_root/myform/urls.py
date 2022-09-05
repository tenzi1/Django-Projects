from django.urls import path
from . import views

urlpatterns = [
    # path('your-name/', views.get_name, name='name'),
    # path('contact-me/', views.contact_form_view, name="contact-me"),
    # path('thanks/', views.name_recieved, name="recieved"),
    # path('article/', views.article_view, name='article'),
    path('article-model', views.get_article, name='get_article'),
    path('author-model', views.get_author, name='get_author')
]