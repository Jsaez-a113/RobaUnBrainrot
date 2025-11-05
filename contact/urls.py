from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('contacto/', views.contact_view, name='contact'),
]
