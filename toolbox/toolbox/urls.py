from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),
    path('character-counter', include('character_counter.urls')),
    path('filler-text', include('filler_text.urls')),
]
