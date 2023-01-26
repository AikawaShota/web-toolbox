from django.shortcuts import render
from .forms import GeneratorForm
from .generator import generator


# Create your views here.
def passwords_generator_view(request):
    form = GeneratorForm
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data["count"]
            number = form.cleaned_data["number"]
            upper = form.cleaned_data["upper"]
            lower = form.cleaned_data["lower"]
            symbol_normal = form.cleaned_data["symbol_normal"]
            symbol_custom = form.cleaned_data["symbol_custom"]
            result = generator(count, number, upper, lower, symbol_normal, symbol_custom)
            context = {
                'form': form,
                'result': result,
            }
            return render(request, 'passwords_generator/index.html', context)
    context = {'form': form}
    return render(request, 'passwords_generator/index.html', context)
