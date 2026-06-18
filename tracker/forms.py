from django import forms
from .models import UserProfile, WaterIntake

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['weight', 'age', 'city', 'activity_level']
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес в кг'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город (на английском)'}),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
        }

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntake
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'мл'}),
        }