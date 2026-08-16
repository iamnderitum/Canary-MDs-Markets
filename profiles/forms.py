from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "bio",
            "phone",
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder":"Tell us about You..."
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder":"+254..."
                }
            ),
            
        }