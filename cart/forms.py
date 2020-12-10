from cart import forms
from django import forms



class QtyForm(forms.Form):

    product_id = forms.CharField(widget=forms.HiddenInput())

    qty = forms.IntegerField(
        min_value = 0,
        max_value = 99,
        widget = forms.TextInput(attrs={'class': 'form-control qty',
                                        'type': 'hidden',
                                      'style': 'text-align: center; color: #705737; background-color: #f3eae0; width: 40px', 
                                      'readonly': 'readonly'}),
        required = True
    )

    