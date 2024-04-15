from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from Member.models import Member

class CustomMemberAdmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'surname', 'category', 'birthday')

# Register the Member model with the custom admin class
admin.site.register(Member, CustomMemberAdmin)

admin.site.register(UserProfile)
