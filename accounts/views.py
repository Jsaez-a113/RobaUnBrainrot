from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import ModeradorRegistrationForm, EditorRegistrationForm


def register_moderador(request):
    """Vista para registro de moderadores"""
    if request.method == 'POST':
        form = ModeradorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f'¡Registro exitoso! Bienvenido {user.first_name}. '
                'Ahora puedes iniciar sesión en el panel de administración.'
            )
            login(request, user)
            return redirect('admin:index')
    else:
        form = ModeradorRegistrationForm()
    
    context = {
        'page_title': 'Registro - Moderador',
        'banner_url': 'https://images.alphacoders.com/139/1396558.jpg',
        'form': form,
        'user_type': 'Moderador',
        'description': 'Los moderadores pueden ver, agregar y editar items brainrot, pero no pueden eliminarlos.',
    }
    return render(request, 'accounts/register.html', context)


def register_editor(request):
    """Vista para registro de editores"""
    if request.method == 'POST':
        form = EditorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f'¡Registro exitoso! Bienvenido {user.first_name}. '
                'Ahora puedes iniciar sesión en el panel de administración.'
            )
            login(request, user)
            return redirect('admin:index')
    else:
        form = EditorRegistrationForm()
    
    context = {
        'page_title': 'Registro - Editor',
        'banner_url': 'https://images.alphacoders.com/139/1396558.jpg',
        'form': form,
        'user_type': 'Editor',
        'description': 'Los editores tienen acceso completo: pueden ver, agregar, editar y eliminar items brainrot.',
    }
    return render(request, 'accounts/register.html', context)
