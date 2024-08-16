from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'price_total', 'discount', 'quantity', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price'}),
            'price_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount amount'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product description'}),
        }
        labels = {
            'name': 'Product name',
            'price': 'Product price',
            'price_total': 'Total price',
            'discount': 'Discount amount',
            'quantity': 'Quantity',
            'description': 'Description'
        }
        help_texts = {
            'discount': 'Enter discount amount. Leave 0 if no discount',
        }
        error_messages = {
            'name': {
                'max_length': 'This name is too long'
            }
        }
