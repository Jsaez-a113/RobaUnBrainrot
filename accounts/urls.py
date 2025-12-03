from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('registro/moderador/', views.register_moderador, name='register_moderador'),
    path('registro/editor/', views.register_editor, name='register_editor'),
]
