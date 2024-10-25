from django import forms
from django.utils.text import slugify
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'finder_no',
            'finder_email',
            'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 4
            }),
            'finder_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter finder number'
            }),
            'finder_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def clean_finder_no(self):
        finder_no = self.cleaned_data.get('finder_no')
        if len(finder_no) != 10:
            raise forms.ValidationError("Finder number must be exactly 10 characters long")
        return finder_no

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Image is required")
        return image