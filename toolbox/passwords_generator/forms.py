from django import forms


class GeneratorForm(forms.Form):
    count = forms.IntegerField(
        min_value=4,
        widget=forms.NumberInput(
            attrs={
                "class": "number_field",
            }
        )
    )
    number = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
            }
        )
    )
    upper = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
            }
        )
    )
    lower = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
            }
        )
    )
    symbol_normal = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
            }
        )
    )
    symbol_custom = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "text_field",
            }
        )
    )
