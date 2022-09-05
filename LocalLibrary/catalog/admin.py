from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


#for inline horizontal layout
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
class BooksInline(admin.TabularInline):
    model = Book

#to change how model is displayed in admin interface we must define ModelAdmin class
class AuthorAdmin(admin.ModelAdmin):
    #controlling which fields are displayed
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    #controlling which fields are laid out in detail view(in form)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    #we can use 'exclude' attr to declare a list of attrs to be excluded from the form
    #(all other attributes in model will be displayed)

    inlines = [BooksInline]
    
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'display_genre')
    
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    #sectioning the detail view
    fieldsets = (
        (None, {
            'fields':('book', 'imprint','id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )

   