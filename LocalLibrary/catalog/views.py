from django.shortcuts import render
from django.test import RequestFactory

# Create your views here.
from .models import Book, Author,BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    nums_visit = request.session.get('nums_visit', 0)
    request.session['nums_visit'] = nums_visit + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'nums_visit': nums_visit
    }

    return render(request, 'index.html', context = context)

# class based list view for 'content/books/'
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    
    #default context is object_list or modelname_list
    # context_object_name = 'book_list'

    # queryset = Book.objects.filter(title__icontains='war')[:5]
    
     #change the list of records returned by overriding get_queryset()
    # def get_queryset(self):
    #     return

    #to pass additional information to template, use get_context_data()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['some_data'] = 'this is additional info'
    #     return context
        
    # template_name = 'books/books_list.html'

   
class BookDetailView(generic.DetailView):
    model = Book

#Author list view
class AuthorListView(generic.ListView):
    model = Author

# Author detail view
class AuthorDetailView(generic.DetailView):
    model = Author

