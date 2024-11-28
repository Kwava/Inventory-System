from django import forms
from .models import Product, Order

 
class CreateProductForm(forms.ModelForm):
    CATEGORY=[('electronics','electronics'),
           ('food','food'),
           ('cosmetics','cosmetics'),
          ]
    class Meta:
        model=Product
        fields=['name','category','quantity']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
        }
    category=forms.ChoiceField(
        choices=CATEGORY,
        widget=forms.Select(attrs={'class':'form-control'})
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model:Order
        fields=['product','order_quantity']
