from django import forms


class FillerTextForm(forms.Form):
    text = forms.fields.ChoiceField(
        choices=(
            ('alice', '不思議の国のアリス'),
            ('constitution_of_japan', '日本国憲法'),
            ('dagon', 'ダゴン'),
            ('frankenstein', 'フランケンシュタイン'),
            ('lorem_ipsum', 'lorem'),
            ('lorem_ipsum_upper', 'lorem（大文字）'),
            ('pangram', 'パングラム'),
            ('rashomon', '羅生門'),
            ('sample', 'サンプルテキスト'),
        ),
        required=True)
    count = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'number_field',
                'value': '0',
            }
        )
    )
    no_space = forms.ChoiceField(
        choices=(
            (0, '有'),
            (1, '無'),
        ),
        widget=forms.Select(),
        required=True,
    )
