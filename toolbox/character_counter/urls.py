from django.urls import path
from . import views

app_name = 'character_counter'
urlpatterns = [
    path('', views.counter_view, name='counter'),
]
