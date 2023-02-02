from django import forms
from .models import FillerTextModel

value_list = [x[0] for x in list(FillerTextModel.objects.all().values_list("value"))]
name_list = [x[0] for x in list(FillerTextModel.objects.all().values_list("name"))]
choices_tuple = tuple(zip(value_list, name_list))


class FillerTextForm(forms.Form):
    text = forms.fields.ChoiceField(
        choices=choices_tuple,
        required=True)
    count = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number_field',
                'value': '200',
            }
        )
    )
    no_space = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'id': 'space'
            }
        ),
        required=False,
    )
