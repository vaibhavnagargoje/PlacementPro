from django.db import models
import os
from datetime import datetime
# Create your models here.



def jd_upload_path(instance,filename):

    current_year = datetime.now().year
    return os.path.join(f'jds/{current_year}/',filename)

class Companies(models.Model):
    company_name = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=255,blank=True)
    website = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_number= models.CharField(max_length=15,blank=True)
    description = models.TextField(blank=True, null=True, help_text="Short description about the company")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class CompanyDrive(models.Model):
    company_name = models.ForeignKey(Companies,on_delete=models.CASCADE,related_name='CompanyDrive')
    job_title = models.CharField(max_length=255,help_text="Drive title (e.g., Software Engineer Hiring)")
    
    drive_date= models.DateField(help_text="Date of the placement Drive")
    applications_starts = models.DateField(auto_now_add=True)
    applications_ends = models.DateField(auto_now_add=True)
    
    job_description=models.FileField(upload_to=jd_upload_path,blank=True, null=True,help_text="Upload Job Description ")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.company_name.company_name} - {self.job_title} ({self.drive_date})"

