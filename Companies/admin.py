from django.contrib import admin
from .models import Companies,CompanyDrive
# Register your models here.

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['company_name','location']
    search_fields= ['company_name','location']


@admin.register(CompanyDrive)
class CompanyDriveAdmin(admin.ModelAdmin):
    list_display =['company_name','job_title','drive_date','applications_ends']
    list_filter = ['company_name__company_name','drive_date','applications_ends']
