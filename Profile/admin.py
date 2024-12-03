from django.contrib import admin
from .models import Profile
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ 

from users.models import Batch



# Register your models here.
from datetime import date
from django.contrib.admin import SimpleListFilter


from datetime import date
from django.contrib.admin import SimpleListFilter
from .models import Batch
from datetime import date
from django.contrib.admin import SimpleListFilter
from .models import Batch

from datetime import date
from django.contrib.admin import SimpleListFilter
from .models import Batch

from datetime import date
from django.contrib.admin import SimpleListFilter
from .models import Batch

class BatchFilter(SimpleListFilter):
    title = 'Batch'
    parameter_name = 'batch'

    def lookups(self, request, model_admin):
        # Determine the current academic year
        current_year = date.today().year
        current_batch = Batch.objects.filter(
            start_year__lte=current_year,
            end_year__gte=current_year
        ).first()

        # Prepare the batch lookups
        batches = Batch.objects.all()

        # Prepare lookups with no 'All' option
        lookups = []

        # Add batch options
        for batch in batches:
            label = f"{batch.start_year}-{batch.end_year}"
            if current_batch and batch.id == current_batch.id:
                label += " (Current Batch)"
            
            lookups.append((batch.id, label))

        return lookups

    def queryset(self, request, queryset):
        if self.value():
            # Ensure the value is an integer, filter by batch
            try:
                batch_id = int(self.value())  # Convert value to integer
                return queryset.filter(profile__batch_id=batch_id)
            except ValueError:
                return queryset  # If value is invalid, show all users

        else:
            # Default to the current academic year if no batch is selected
            current_year = date.today().year
            return queryset.filter(
                profile__batch__start_year__lte=current_year,
                profile__batch__end_year__gte=current_year
            )


@admin.register(Batch)
class BatchAdmin(ModelAdmin):
    list_filter =['start_year']

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user_id','first_name','last_name','role','batch']
    search_fields = ['user__username','user__first_name','user__last_name','user__email',]
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