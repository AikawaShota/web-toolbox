from django.shortcuts import render
from .forms import FillerTextForm
from .text import filler_text


def filler_text_view(request):
    form = FillerTextForm
    if request.method == "POST":
        form = FillerTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            count = form.cleaned_data["count"]
            no_space = bool(int(form.cleaned_data["no_space"]))
            result = filler_text(text, count, no_space)
            context = {
                'form': form,
                'result': result,
            }
            return render(request, 'filler_text/index.html', context)
    context = {'form': form}
    return render(request, 'filler_text/index.html', context)
