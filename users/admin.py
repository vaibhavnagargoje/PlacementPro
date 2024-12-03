from django.contrib import admin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from .resources import UserResource
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


from .filters import BatchFilter  # Import the custom filter from the filters.py

# Unregister the default User admin
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin,ModelAdmin, ImportExportModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    resource_class = UserResource
    import_form_class = ImportForm  # Use Unfold-styled ImportForm
    export_form_class = ExportForm
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active',BatchFilter)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    ordering = ('username',)




# admin.py

from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin


admin.site.unregister(Group)



@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass