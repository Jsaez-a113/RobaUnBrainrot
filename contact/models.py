from django.db import models


class ContactMessage(models.Model):
    """Modelo para almacenar mensajes de contacto"""
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo electrónico")
    subject = models.CharField(max_length=200, verbose_name="Asunto")
    message = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    is_read = models.BooleanField(default=False, verbose_name="Leído")
    
    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-created']
    
    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"
