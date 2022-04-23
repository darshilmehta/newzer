from django import forms
from .models import LocalNews

class LocalNewsForm(forms.ModelForm):
    class Meta:
        model = LocalNews
        fields = ['name', 'title', 'content', 'image_url', 'country_name']