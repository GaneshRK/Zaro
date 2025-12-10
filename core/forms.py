from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone']

    # Save both User and Profile
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Create profile with phone number
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone']
            )

        return user
