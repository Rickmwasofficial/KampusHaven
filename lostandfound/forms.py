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
            'image',
            'location'
        ]
        name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
                'placeholder': 'Enter product name'
            })
        )
        location = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
                'placeholder': 'Enter place found'
            })
        )
        description = forms.CharField(
            widget=forms.Textarea(attrs={
                'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
                'placeholder': 'Enter item description',
                'rows': 4
            })
        )
        finder_no = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
                'placeholder': 'Enter your number'
            })
        )
        finder_email = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
                'placeholder': 'Enter your email'
            })
        )
        image = forms.ImageField(
            required=True,
            widget=forms.FileInput(
                attrs={
                    'id': 'upload',
                    'class': 'hidden',
                    'accept': 'image/*'
                }
            )
        )


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