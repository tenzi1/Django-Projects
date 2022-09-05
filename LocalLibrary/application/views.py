from msilib.schema import ListView
from django.views import generic
from .models import Publisher

class PublisherListView(generic.ListView):
    model = Publisher

    # this view will look for 'application/publisher_list.html by default
    