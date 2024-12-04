from django.shortcuts import render

# Create your views here.



def Profile(request):

    return render(request,'profile/profile.html')


from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SimplePasswordChangeForm

@login_required
def change_password(request):
    if request.method == "POST":
        form = SimplePasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # Update the user's password
            new_password = form.cleaned_data["new_password"]
            request.user.set_password(new_password)
            request.user.save()

            # Keep the user logged in after password change
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password has been updated successfully!")
            return redirect('dashboard')  # Redirect to profile or any other page
        else:
            # If the form has errors, display them
            messages.error(request, "Please correct the errors below.")
    else:
        form = SimplePasswordChangeForm(user=request.user)

    return render(request, 'profile/change_password.html', {'form': form})