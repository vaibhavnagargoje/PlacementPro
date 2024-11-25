from django.contrib import admin
from .models import Companies,CompanyDrive
from unfold.admin import ModelAdmin


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.forms import  UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from django.contrib.admin import register
from django.contrib.auth.models import User,Group
admin.site.unregister(User)
# admin.site.unregister(Group)

@register(User)
class UserAdmin(BaseUserAdmin,ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

# Register your models here.

@admin.register(Companies)
class CompaniesAdmin(ModelAdmin):
    list_display = ['company_name','location']
    search_fields= ['company_name','location']


@admin.register(CompanyDrive)
class CompanyDriveAdmin(ModelAdmin):
    list_display =['company_name','job_title','drive_date','applications_ends']
    list_filter = ['company_name__company_name','drive_date','applications_ends']




