from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """Vista para el formulario de contacto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje (aunque no sea funcional, guardamos para mostrar que funciona)
            contact_message = form.save()
            messages.success(
                request, 
                f'¡Gracias {contact_message.name}! Tu mensaje ha sido enviado correctamente. '
                'Te responderemos pronto.'
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
