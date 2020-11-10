from django import forms

class FormSearchProduct(forms.Form):

    name = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False
    )

    #<input type="text" name="name" id="id_name" class="form-control form-control-sm" maxlength="100">
        