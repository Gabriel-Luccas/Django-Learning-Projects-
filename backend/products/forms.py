from django import forms
from .models import Product


class Form(forms.ModelForms):
    class Meta:
        model = Product
        fields = ["title", "content", "price"]
