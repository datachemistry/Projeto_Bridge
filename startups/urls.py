from django.urls import path
from startups.views import index, startup

urlpatterns = [
    path('', index, name="index"),
    path('imagem/', startup, name="startup"),
]