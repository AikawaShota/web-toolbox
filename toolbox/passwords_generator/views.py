from django.shortcuts import render

# Create your views here.
def passwords_generator_view(request):
    return render(request, 'passwords_generator/index.html')