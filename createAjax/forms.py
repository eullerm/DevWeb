from django import forms
from createAjax.models import ProductAjax
from category.models import Category
from web_project import settings
from django.core.validators import RegexValidator
from createAjax.mixin import AjaxFormMixin

class ProductFormAjax(forms.ModelForm):

     
    class Meta:
        model = ProductAjax
        fields = ('name','category', 'price', 'quantity')
        localized_field = ('price',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].error_messages={'required': 'Campo obrigatório', 
                                            'unique': 'Nome de produto duplicado'}
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '100'})


        self.fields['category'].error_messages={'required': 'Campo obrigatório'}
        self.fields['category'].queryset=Category.objects.all().order_by('name')
        self.fields['category'].empty_label="------Selecione uma categoria------"
        self.fields['category'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['price'].min_value = 0
        self.fields['price'].error_messages={'required': 'Campo obrigatório', 
            'invalid': 'Preço inválido.', 
            'min-value':'O preço deve ser maior ou igual a zero', 
            'max_digits': 'Mais de 5 digitos no total',
            'max_decimal_places': 'Mais de 2 digitos decimais.', 
            'max_whole_digits': 'Mais de 3 digitos inteiros.',
        }
        self.fields['price'].widget.attrs.update({'class': 'form-control form-control-sm',
                                                    'onekeypress': 'return (event.charCode >= 48 && event.charCode <= 57 || event.charCode == 44',})

        self.fields['quantity'].min_value = 0
        self.fields['quantity'].max_value = 99
        self.fields['quantity'].error_messages={'required': 'Campo obrigatório', 
            'invalid': 'Quantidade inválida.', 
            'min-value':'A quantidade deve ser maior ou igual a zero', 
            'max_digits': 'Mais de 5 digitos no total',
            'max_decimal_places': 'Mais de 2 digitos decimais.',
            'max_whole_digits': 'Mais de 10 digitos inteiros.',
        }
        self.fields['quantity'].widget.attrs.update({'class': 'form-control form-control-sm',
                                                    'onekeypress': 'return (event.charCode >= 48 && event.charCode <= 57 || event.charCode == 44',})

class QuantityForm(forms.Form):

    productId = forms.CharField(widget=forms.HiddenInput())

    quantity = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control btn-light quantity mx-auto',
                                      'style': 'text-align: center; background-color: white; width: 70px;',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
        required=True
    )