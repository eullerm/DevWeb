from django import forms
from category.models import Category
from web_project import settings
from django.core.validators import RegexValidator

class FormSearchCategory(forms.Form):

    name = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '70'}),
        required=False
    )

    #<input type="text" name="name" id="id_name" class="form-control form-control-sm" maxlength="100">
        
class CategoryForm(forms.ModelForm):

     
    class Meta:
        model = Category
        fields = ('name',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].error_messages={'required': 'Campo obrigatório', 
                                            'unique': 'Nome de categoria duplicado'
                                            }
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm', 'maxlength': '70'})