from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quienes-somos/', views.about, name='about'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('galeria/', views.gallery, name='gallery'),
    path('', include('brainrot.urls')),
    path('', include('contact.urls')),
    path('', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('', include('api_consumer.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Catch-all para 404 personalizado (solo en desarrollo, al final)
    urlpatterns += [
        path('<path:path>', views.custom_404, name='404'),
    ]