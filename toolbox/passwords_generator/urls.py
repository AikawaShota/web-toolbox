from django.urls import path
from . import views

app_name = 'passwords_generator'
urlpatterns = [
    path('', views.passwords_generator_view, name='passwords_generator'),
]
