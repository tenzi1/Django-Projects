from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Dweet

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    #only display the 'username' field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

#register Profile model to admin
# admin.site.register(Profile)

admin.site.register(Dweet)