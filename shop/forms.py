from django import forms
from shop.models import Information

class createform(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'
