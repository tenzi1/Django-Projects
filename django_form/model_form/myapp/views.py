from django.shortcuts import redirect, render
from .forms import EmpDetailsForm

def emp_form(request):
    if request.method == 'POST':
        form = EmpDetailsForm(request.POST)
        if form.is_valid():
            print('validated')
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Contact = form.cleaned_data['Contact']
            print('Name:', Name)
            print('Email:', Email)
            print('Conatct:', Contact)
    else:
        form = EmpDetailsForm()
    return render(request, 'form.html', {'form':form})
