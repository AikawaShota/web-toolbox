from django.urls import path, include
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('character_counter', include('character_counter.urls')),
]
