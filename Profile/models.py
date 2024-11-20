from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Student','Student'),
        ('CR',"Class Representative"),
        ('Officer',"Placement Officer"),
    ]
    DepartmentChoices = [
        ('CS','Computer Science',),
        ('CA','Computer Applications'),
        ('DS','Data Science')
    ]

    user  = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='Student')
    mobile_number = models.CharField(max_length=15,blank=True, null=True)
    department = models.CharField(max_length=50,choices=DepartmentChoices,blank=True)
    cgpa_graduation = models.DecimalField(max_digits=4,decimal_places=2,null=tuple,blank=True)
    cgpa_post_graduation=models.DecimalField(max_digits=4,decimal_places=2,null=True, blank=True)
    project_graduation = models.TextField(blank=True, help_text='Project name and used Technoloy for projects')
    project_post_graduation = models.TextField(blank=True, help_text='Project name and used Technoloy for projects')

    resume = models.URLField(blank=True,help_text='Link to resume(e.g., google drive link)')



    #meta information 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} -  {self.role}"
