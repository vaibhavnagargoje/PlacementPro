from django.contrib import admin
from .models import Profile
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ 

from users.models import Batch



# Register your models here.
from datetime import date
from django.contrib.admin import SimpleListFilter

class BatchFilter(SimpleListFilter):
    title = 'Batch'
    parameter_name = 'batch'

    def lookups(self, request, model_admin):
        # Provide a list of all available batches and an 'All' option
        batches = Batch.objects.all()
        return [('all', 'All')] + [
            (batch.id, f"{batch.start_year}-{batch.end_year}") for batch in batches
        ]

    def queryset(self, request, queryset):
        if self.value() == 'all':
            return queryset  # Show all users
        elif self.value():
            return queryset.filter(profile__batch_id=self.value())  # Filter users by batch
        else:
            # Default to the current academic year
            current_year = date.today().year
            return queryset.filter(
                profile__batch__start_year__lte=current_year,
                profile__batch__end_year__gte=current_year
            )
        
        
@admin.register(Batch)
class BatchAdmin(ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user_id','first_name','last_name','role','batch']
    search_fields = ['user__username','user__first_name','user__last_name','user__email','batch_name']
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