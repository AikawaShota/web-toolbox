from django.urls import path, include
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('character-counter', include('character_counter.urls')),
    path('filler-text', include('filler_text.urls')),
]
