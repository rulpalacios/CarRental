from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'cost': forms.TextInput(attrs={'class': 'input'}),
            'image': forms.FileInput(attrs={'class': 'file-input'}),
            'seats': forms.TextInput(attrs={'class': 'input'}),
            'slug': forms.TextInput(attrs={'class': 'input'})
        }
