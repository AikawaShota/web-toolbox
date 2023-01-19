from django.shortcuts import render
from .forms import CounterForm
from . import counter


# 文字数カウント
def counter_view(request):
    form = CounterForm
    if request.method == "POST":
        form = CounterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            result = counter.character_counter(text)
            context = {
                'form': form,
                'text': text,
                'number_of_character': result[0],
                'no_space': result[1],
                'manuscript_paper': result[2],
            }
            return render(request, 'character_counter/index.html', context)
    context = {'form': form}
    return render(request, 'character_counter/index.html', context)
