from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "bio",
            "city",
            "address",
            "dob",
            "phone",
            "profession", 
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder":"Tell us about You..."
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter City",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Address"
                }
            ),
            "dob": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+254...",
                }
            ),
            
            "phone": forms.TextInput(
                attrs={
                    "placeholder":"+254..."
                }
            ),
            "profession":forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            
        }

        labels = {
            "bio": "Bio",
            "image": "Upload Profile Image",
            "city": "City",
            "address": "Address",
            "dob": "Date Of Birth",
            "phone": "Phone",
            "profession": "Profession"
        }