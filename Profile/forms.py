from django import forms
from django.contrib.auth.models import User

class SimplePasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 bg-gray-700 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            'placeholder': 'Enter your old password',
        }),
        label="Old Password",
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 bg-gray-700 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            'placeholder': 'Enter a new password',
        }),
        label="New Password",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 bg-gray-700 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            'placeholder': 'Confirm new password',
        }),
        label="Confirm New Password",
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("The old password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        
        # Check if new password and confirm password match
        if new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")
        
        # Optionally, you can add additional validation for password strength here
        if len(new_password) < 8:
            raise forms.ValidationError("The new password must contain at least 8 characters.")

        return cleaned_data
