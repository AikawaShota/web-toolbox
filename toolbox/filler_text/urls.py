from django.urls import path
from . import views

app_name = 'filler_text'
urlpatterns = [
    path('', views.filler_text_view, name='filler_text'),
]
