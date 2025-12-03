from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    """Vista para el formulario de contacto con envío a Mailtrap"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje en la base de datos
            contact_message = form.save()
            
            # Enviar email a Mailtrap
            try:
                send_mail(
                    subject=f'[Roba un Brainrot] {contact_message.subject}',
                    message=f'''
Nombre: {contact_message.name}
Email: {contact_message.email}
Asunto: {contact_message.subject}

Mensaje:
{contact_message.message}

---
Este mensaje fue enviado desde el formulario de contacto de Roba un Brainrot.
Fecha: {contact_message.created.strftime("%d/%m/%Y %H:%M:%S")}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(
                    request, 
                    f'¡Gracias {contact_message.name}! Tu mensaje ha sido enviado correctamente a nuestro equipo. '
                    'Te responderemos pronto.'
                )
            except Exception as e:
                # Si falla el envío, aún guardamos el mensaje
                messages.warning(
                    request,
                    f'Tu mensaje se ha guardado, pero hubo un problema al enviarlo. '
                    f'Error: {str(e)}'
                )
            
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'page_title': 'Roba un Brainrot - Contacto',
        'banner_url': 'https://images.alphacoders.com/139/1396558.jpg',
        'form': form,
    }
    return render(request, 'contact/contact.html', context)