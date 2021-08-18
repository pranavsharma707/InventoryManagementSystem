from django import forms
from .models import Product,Order,FileUpload

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FileUpload
        fields=['file_upload']