from django import forms


class CounterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'text_field',
            'placeholder': 'カウントしたい文章を入力してください',
            'cols': '64',
            'lows': '10',
        }))
