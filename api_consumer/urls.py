from django.urls import path
from . import views

app_name = "api_consumer"

urlpatterns = [
    path('api-items/', views.api_items_view, name='api_items'),
]
