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
                "id": "number",
            }
        )
    )
    upper = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
                "id": "upper",
            }
        )
    )
    lower = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
                "id": "lower",
            }
        )
    )
    symbol_normal = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox_field",
                "id": "symbol-normal",
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
