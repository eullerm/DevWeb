from django import forms
from product.models import Product
from category.models import Category
from web_project import settings
from django.core.validators import RegexValidator

class FormSearchProduct(forms.Form):

    name = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False
    )

    #<input type="text" name="name" id="id_name" class="form-control form-control-sm" maxlength="100">
        
class ProductForm(forms.ModelForm):

     
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'registeredDate', 'price', 'image', 'available', 'bestSeller', 'steel', 'color')
        localized_field = ('price',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].error_messages={'required': 'Campo obrigatório', 
                                            'unique': 'Nome de produto duplicado'
                                            }
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '100'})

        self.fields['description'].error_messages={'required': 'Campo obrigatório'}
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '100'})

        self.fields['category'].error_messages={'required': 'Campo obrigatório'}
        self.fields['category'].queryset=Category.objects.all().order_by('name')
        self.fields['category'].empty_label="------Selecione uma categoria------"
        self.fields['category'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['registeredDate'].input_formats=settings.DATE_INPUT_FORMATS
        self.fields['registeredDate'].error_messages={'required': 'Campo obrigatório', 
                                                    'invalid': 'Data inválida.'
                                                    }
        self.fields['registeredDate'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['price'].min_value = 0
        self.fields['price'].error_messages={'required': 'Campo obrigatório', 
            'invalid': 'Preço inválido.', 
            'min-value':'O preço deve ser maior ou igual a zero', 
            'max_digits': 'Mais de 5 digitos no total',
            'max_decimal_places': 'Mais de 2 digitos decimais.', 
            'max_whole_digits': 'Mais de 3 digitos inteiros.',
        }
        self.fields['price'].widget.attrs.update({'class': 'form-control form-control-sm',
                                                    'onekeypress': 'return (event.charCode >= 48 && event.charCode <= 57 || event.charCode == 44',
                                                })

        # self.fields['image'].error_messages={'required': 'Campo obrigatório'}
        # self.fields['image'].validators = [RegexValidator(regex='^[aA-zZ-]+[0-9]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        # self.fields['image'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '50'})
        # self.fields['image'].required = True

        
        self.fields['image'].error_messages={'required': 'Campo obrigatório', 
                                            'invalid_image': "Imagem inválida"}
        self.fields['image'].widget.attrs.update({'class': 'btn btn-outline-secundary btn-sm'})

        self.fields['steel'].error_messages={'required': 'Campo obrigatório'}
        self.fields['steel'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['color'].error_messages={'required': 'Campo obrigatório'}
        self.fields['color'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '100'})


