from django.shortcuts import render
from .forms import CounterForm


# 文字数カウント
def counter(request):
    form = CounterForm
    if request.method == "POST":
        form = CounterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            number_of_character = len(text)
            context = {
                'form': form,
                'text': text,
                'number_of_character': f'文字数は、{number_of_character}文字です。',
            }
            return render(request, 'character_counter/index.html', context)
    context = {'form': form}
    return render(request, 'character_counter/index.html', context)
