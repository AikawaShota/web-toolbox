from django import forms


class CounterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
