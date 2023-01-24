from django.shortcuts import render


def filler_text_view(request):
    return render(request, 'filler_text/index.html')
