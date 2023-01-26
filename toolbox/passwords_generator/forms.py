from django import forms


class GeneratorForm(forms.Form):
    count = forms.IntegerField(min_value=4)
    number = forms.BooleanField(required=False)
    upper = forms.BooleanField(required=False)
    lower = forms.BooleanField(required=False)
    symbol_normal = forms.BooleanField(required=False)
    symbol_custom = forms.CharField(required=False)
