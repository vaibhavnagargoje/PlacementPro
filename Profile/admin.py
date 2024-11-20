from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id','first_name','last_name','role']
    search_fields = ['user__username','user__first_name','user__last_name','user__email']
    list_filter = ['role','department']

    def user_id(self,obj):
        return obj.user.username
    user_id.short_description = "User ID "

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First Name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last Name'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'