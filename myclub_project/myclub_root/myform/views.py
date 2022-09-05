from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.forms import  formset_factory
from . import forms
def name_recieved(request):
    return render(request, 'name_recieved.html', {})

# creating Model Form
from django.forms import ModelForm
from .models import Article, Book, Author

#create model form for Author Model
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name','title']

#create model form for Book Model
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

#view for rendering model forms
def get_author(request):
    print(request.POST)
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        print('validating')
        if author_form.is_valid():
            print('form data is valid')
            
            return HttpResponse(author_form.cleaned_data)
        else:
            print('invalid form data')
            return HttpResponse(author_form.errors)
    else:
        author_form = AuthorForm()
    return render(request, 'author_model_form.html', {'author_form':author_form})
#create form class
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']

def get_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data)
        else:
            return HttpResponse(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'article_model_form.html', {'form':form})




# def get_name(request):
#     #check if the request is post
#     if request.method == 'POST':
#         #instantiate the form with user submitted data
#         form = forms.NameForm(request.POST)
#         # check if all the data are valid:
#         if form.is_valid():
#             #process the form data
#             #...
#             #redirect to another page
#             return HttpResponseRedirect('/thanks/')
#     #else if the request is GET or any other
#     else:
#         #create empty form and return it
#         form = forms.NameForm()
#     return render(request, 'name.html', {'form': form})

# # processing Contact Form

# from django.core.mail import send_mail

# def contact_form_view(request):
#     if request.method == 'POST':
#         form = forms.ContactForm(request.POST)
#         if form.is_valid():
#             # if true the submitted data will be in forms.cleaned_data dict
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             sender = form.cleaned_data['sender']
#             cc_myself = form.cleaned_data['cc_myself']

#             recipients = ['sherpatshering783@gmail.com']
#             if cc_myself:
#                 recipients.append(sender)
            
#             send_mail(subject, message, sender, recipients)
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = forms.ContactForm
        
    
#     return render(request, 'contact_form.html', {'form':form})


# #  formset for article form
# # import datetime
# # def article_view(request):
# #     ArticleFormset = formset_factory(forms.ArticleForm, max_num=1)
# #     if request.method=='POST':
# #         formset = ArticleFormset(request.POST)
# #         print(request.POST)
# #         print(formset)
# #         # return HttpResponse(formset.cleaned_data)
# #         return HttpResponse(formset.empty_form)
    
# #     formset = ArticleFormset(initial=[{'title':'django formset','pub_date':'2022-07-07'}])   
   
# #     return render(request, 'article.html', {'formset':formset})

# # custom formset validation
# from django.core.exceptions import ValidationError
# from django.forms import BaseFormSet,formset_factory
# # from .forms import ArticleForm

# class BaseArticleFormSet(BaseFormSet):
#     def clean(self):
#         """checks that no two article has same title."""
#         if any(self.errors):
#             #don't bother validating the formset unless each form is valid on its own
#             return
#         titles = []
#         for form in self.forms:
#             if self.can_delete and self._should_delete_form(form):
#                 continue
#             title = form.cleaned_data.get('title')
#             if title in titles:
#                 raise ValidationError('Articles in a set must have distict titles')
#             titles.append(title)

# # using baseformset in formset
# def article_view(request):
#     ArticleFormset = formset_factory(forms.ArticleForm, formset=BaseArticleFormSet,extra=1)
#     if request.method=='POST':
#         formset = ArticleFormset(request.POST)
       
#         return HttpResponse(formset.non_form_errors())
       
        
        
       
    
#     formset = ArticleFormset(initial=[{'title':'django formset','pub_date':'2022-07-07'}])   
   
#     return render(request, 'article.html', {'formset':formset})

