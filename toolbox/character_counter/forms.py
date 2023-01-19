from django import forms


class CounterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'text_field',
            'placeholder': '文字数をカウントしたい文章をここに入力。',
            'cols': '64',
            'lows': '10',
        }))
