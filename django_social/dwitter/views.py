from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DweetForm
from .models import Profile, Dweet

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect('dwitter:dashboard')
    
    if request.user.is_authenticated:
        followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-created_at')

        return render(request, "dwitter/dashboard.html", {'form':form,
    'dweets': followed_dweets})
    else:
        return render(request, "dwitter/dashboard.html",{})
    
    

def profile_list(request):
    profiles = Profile.objects.all()
   
    return render(request, "dwitter/profile_list.html", {"profiles":profiles})
    
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)

    #handling the button data
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    
    
    return render(request, "dwitter/profile.html", {"profile":profile})