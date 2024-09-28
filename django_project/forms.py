from django import forms

from .models import Thing


class ProductForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ['name', 'manufacturer', 'cost', 'weight', 'image']
