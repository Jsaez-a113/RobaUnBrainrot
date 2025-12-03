from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('items/', views.brainrot_items, name='brainrot_items'),
]
