from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from crispy_forms.bootstrap import Field
from brainrot.models import BrainrotItem


class ModeradorRegistrationForm(UserCreationForm):
    """Formulario de registro para Moderadores"""
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('username', css_class='form-group mb-3'),
            Field('email', css_class='form-group mb-3'),
            Field('password1', css_class='form-group mb-3'),
            Field('password2', css_class='form-group mb-3'),
            HTML('<hr class="my-4">'),
            Submit('submit', 'Registrarse como Moderador', css_class='btn btn-primary btn-lg w-100'),
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Crear o obtener grupo Moderadores
            group, created = Group.objects.get_or_create(name='Moderadores')
            
            # Si el grupo se acaba de crear, asignar permisos
            if created:
                content_type = ContentType.objects.get_for_model(BrainrotItem)
                # Permisos para moderadores: ver, cambiar, agregar (pero no eliminar)
                permissions = Permission.objects.filter(
                    content_type=content_type,
                    codename__in=['view_brainrotitem', 'change_brainrotitem', 'add_brainrotitem']
                )
                group.permissions.set(permissions)
            
            # Asignar usuario al grupo
            user.groups.add(group)
            # Dar permisos de staff para acceder al admin
            user.is_staff = True
            user.save()
        
        return user


class EditorRegistrationForm(UserCreationForm):
    """Formulario de registro para Editores"""
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Field('username', css_class='form-group mb-3'),
            Field('email', css_class='form-group mb-3'),
            Field('password1', css_class='form-group mb-3'),
            Field('password2', css_class='form-group mb-3'),
            HTML('<hr class="my-4">'),
            Submit('submit', 'Registrarse como Editor', css_class='btn btn-success btn-lg w-100'),
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Crear o obtener grupo Editores
            group, created = Group.objects.get_or_create(name='Editores')
            
            # Si el grupo se acaba de crear, asignar permisos
            if created:
                content_type = ContentType.objects.get_for_model(BrainrotItem)
                # Permisos para editores: ver, agregar, cambiar y eliminar (todos los permisos)
                permissions = Permission.objects.filter(
                    content_type=content_type
                )
                group.permissions.set(permissions)
            
            # Asignar usuario al grupo
            user.groups.add(group)
            # Dar permisos de staff para acceder al admin
            user.is_staff = True
            user.save()
        
        return user
