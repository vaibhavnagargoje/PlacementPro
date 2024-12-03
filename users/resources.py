from import_export import resources, fields
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserResource(resources.ModelResource):
    password = fields.Field(column_name='password')  # Explicitly define password column

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')  # Exclude 'id'
        export_order = ('username', 'email', 'first_name', 'last_name', 'password')
        skip_unchanged = True
        report_skipped = True

    def dehydrate_password(self, user):
        """
        During export, set the password field to the username value.
        """
        return user.username  # Export the password as the username

    def before_save_instance(self, instance, row, **kwargs):
        """
        Before saving, ensure the password is hashed during import.
        If password is not provided, set it to the username.
        """
        if not instance.password:  # If no password is provided, set the password as the username
            instance.password = instance.username  # Default password is the username
        if not instance.password.startswith('pbkdf2_'):  # Check if password is already hashed
            instance.password = make_password(instance.password)  # Hash the password
        
        super().before_save_instance(instance, row, **kwargs)  # Pass row and kwargs to the parent method

    def get_instance(self, instance_loader, row):
        """
        Override get_instance to prevent 'id' column from causing issues.
        We'll rely on the 'username' column to identify existing instances.
        """
        username = row.get('username', None)
        if not username:
            raise ValueError("Missing 'username' field in import row.")
        
        # Attempt to fetch an existing user by 'username', otherwise create a new one
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return User(username=username)
