# Instrucciones para Funcionalidades Avanzadas

## 📋 Requisitos Previos

### 1. Instalar Dependencias

```bash
pip install django-crispy-forms crispy-bootstrap5 djangorestframework requests Pillow
```

### 2. Crear y Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔐 1. Grupos y Usuarios con Permisos

### Configuración Automática

Los grupos se crean automáticamente cuando el primer usuario se registra en cada tipo.

### Grupos Creados:

1. **Moderadores**:
   - Permisos: Ver, Agregar y Editar items brainrot
   - **NO pueden eliminar** items
   - Acceso al panel de administración

2. **Editores**:
   - Permisos: Ver, Agregar, Editar y **Eliminar** items brainrot
   - Acceso completo al panel de administración

### URLs de Registro:

- **Moderador**: `http://127.0.0.1:8000/registro/moderador/`
- **Editor**: `http://127.0.0.1:8000/registro/editor/`

### Funcionamiento:

1. El usuario completa el formulario de registro
2. Si el grupo no existe, se crea automáticamente con los permisos correspondientes
3. Si el grupo ya existe, solo se asigna el usuario al grupo
4. El usuario queda con `is_staff=True` para acceder al admin
5. Después del registro, el usuario es redirigido al panel de administración

### Probar:

1. Ve a `/registro/moderador/` y crea un usuario moderador
2. Ve a `/registro/editor/` y crea un usuario editor
3. Inicia sesión en `/admin/` con cada usuario
4. Verifica que los permisos sean diferentes:
   - Moderador: No verá la opción de eliminar items
   - Editor: Verá todas las opciones incluyendo eliminar

---

## 📧 2. Formulario de Contacto con Mailtrap

### Configuración de Mailtrap:

1. **Crear cuenta en Mailtrap**:
   - Ve a: https://mailtrap.io/
   - Crea una cuenta gratuita
   - Ve a "Email Testing" → "Inboxes" → "SMTP Settings"

2. **Obtener credenciales**:
   - Copia el **Username** (usuario)
   - Copia el **Password** (contraseña)

3. **Configurar en Django**:
   - Abre `RobaUnBrainrot/settings.py`
   - Busca las líneas:
     ```python
     EMAIL_HOST_USER = 'tu_usuario_mailtrap'
     EMAIL_HOST_PASSWORD = 'tu_password_mailtrap'
     ```
   - Reemplaza con tus credenciales reales de Mailtrap

### Probar el Envío de Emails:

1. Ve a: `http://127.0.0.1:8000/contacto/`
2. Completa el formulario de contacto
3. Envía el mensaje
4. Ve a tu cuenta de Mailtrap → "Inboxes" → "Sandbox"
5. Deberías ver el email recibido con el mensaje de contacto

### Estructura del Email:

- **Asunto**: `[Roba un Brainrot] {asunto del mensaje}`
- **Contenido**: Incluye nombre, email, asunto, mensaje y fecha

---

## 🔌 3. API REST

### Endpoints Disponibles:

#### GET - Obtener todos los items
```
GET http://127.0.0.1:8000/api/items/
```

**Respuesta**:
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "name": "Nombre del item",
      "description": "Descripción",
      "img_url": "http://127.0.0.1:8000/media/brainrot_images/imagen.jpg",
      "category_name": "Categoría",
      "is_featured": true,
      "views_count": 5,
      "created": "2025-01-15T10:30:00Z",
      "updated": "2025-01-15T10:30:00Z"
    }
  ]
}
```

#### POST - Crear un nuevo item
```
POST http://127.0.0.1:8000/api/items/
Content-Type: application/json

{
  "name": "Nuevo Item",
  "description": "Descripción del nuevo item",
  "category": 1,
  "is_featured": false
}
```

**Nota**: Para subir imágenes, usa `multipart/form-data` en lugar de JSON.

### Probar la API:

#### Con cURL:
```bash
# GET
curl http://127.0.0.1:8000/api/items/

# POST
curl -X POST http://127.0.0.1:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item", "description": "Descripción de prueba", "category": 1}'
```

#### Con Python requests:
```python
import requests

# GET
response = requests.get('http://127.0.0.1:8000/api/items/')
print(response.json())

# POST
data = {
    "name": "Item desde API",
    "description": "Creado mediante POST",
    "category": 1,
    "is_featured": False
}
response = requests.post('http://127.0.0.1:8000/api/items/', json=data)
print(response.json())
```

#### Con Postman o Insomnia:
- URL: `http://127.0.0.1:8000/api/items/`
- Método: GET o POST
- Headers: `Content-Type: application/json` (para POST)
- Body: JSON con los datos (para POST)

---

## 🌐 4. Consumir API desde la Web

### Vista que Consume la API:

- **URL**: `http://127.0.0.1:8000/api-items/`
- **Funcionalidad**: Consume el endpoint GET de la API y muestra los items en la web

### Características:

- Muestra todos los items obtenidos de la API
- Maneja errores si la API no está disponible
- Muestra información sobre el endpoint de la API
- Diseño coherente con el resto del sitio

### Probar:

1. Asegúrate de tener items en la base de datos
2. Ve a: `http://127.0.0.1:8000/api-items/`
3. Deberías ver los items obtenidos desde la API REST

---

## 📁 Estructura de Apps Creadas

### `accounts/`
- **Formularios de registro** para Moderadores y Editores
- **Creación automática de grupos** con permisos
- **Asignación de usuarios** a grupos

### `api/`
- **Endpoints REST** (GET y POST)
- **Serializers** para BrainrotItem
- **Sin autenticación** requerida

### `api_consumer/`
- **Vista que consume la API** local
- **Muestra items** obtenidos desde la API
- **Manejo de errores** si la API no está disponible

### `contact/` (actualizado)
- **Envío de emails** a Mailtrap
- **Guardado en base de datos**
- **Mensajes de confirmación**

---

## 🔧 Configuración Final

### 1. Actualizar Settings.py

Ya está configurado, solo necesitas:
- Agregar tus credenciales de Mailtrap (líneas 157-158)

### 2. Verificar URLs

Todas las URLs están configuradas en `RobaUnBrainrot/urls.py`:
- `/registro/moderador/` - Registro moderador
- `/registro/editor/` - Registro editor
- `/api/items/` - API REST
- `/api-items/` - Consumir API desde web
- `/contacto/` - Formulario de contacto

### 3. Reiniciar Servidor

```bash
python manage.py runserver
```

---

## ✅ Checklist de Verificación

### Grupos y Usuarios:
- [ ] Crear usuario moderador desde `/registro/moderador/`
- [ ] Verificar que el grupo "Moderadores" se creó en el admin
- [ ] Verificar permisos del moderador (no puede eliminar)
- [ ] Crear usuario editor desde `/registro/editor/`
- [ ] Verificar que el grupo "Editores" se creó en el admin
- [ ] Verificar permisos del editor (puede eliminar)

### Mailtrap:
- [ ] Configurar credenciales en settings.py
- [ ] Enviar mensaje desde `/contacto/`
- [ ] Verificar email en Mailtrap Sandbox

### API REST:
- [ ] Probar GET en `/api/items/`
- [ ] Probar POST en `/api/items/`
- [ ] Verificar que los datos se guardan correctamente

### Consumir API:
- [ ] Visitar `/api-items/`
- [ ] Verificar que muestra items desde la API
- [ ] Verificar manejo de errores si la API falla

---

## 🐛 Solución de Problemas

### Error: "No module named 'rest_framework'"
**Solución**: `pip install djangorestframework`

### Error: "No module named 'requests'"
**Solución**: `pip install requests`

### Emails no se envían:
1. Verifica credenciales de Mailtrap en settings.py
2. Verifica que `EMAIL_HOST_USER` y `EMAIL_HOST_PASSWORD` estén correctos
3. Revisa la consola del servidor para errores

### API no responde:
1. Verifica que el servidor esté corriendo
2. Verifica que la URL sea correcta: `/api/items/`
3. Revisa la consola del servidor para errores

### Usuarios no pueden acceder al admin:
1. Verifica que `is_staff=True` se haya asignado (se hace automáticamente)
2. Verifica que el usuario esté en un grupo
3. Verifica que el grupo tenga permisos asignados

---

## 📝 Notas Importantes

1. **Mailtrap**: Es un servicio de prueba de emails, perfecto para desarrollo. Los emails no se envían realmente, solo se capturan en su sandbox.

2. **API sin autenticación**: La API está configurada sin autenticación para facilitar las pruebas. En producción, deberías agregar autenticación.

3. **Grupos automáticos**: Los grupos se crean automáticamente la primera vez que alguien se registra. No necesitas crearlos manualmente.

4. **Permisos**: Los permisos se asignan automáticamente según el tipo de usuario:
   - Moderadores: view, add, change (NO delete)
   - Editores: view, add, change, delete (todos)

---

## 🎉 ¡Listo!

Ahora tienes todas las funcionalidades avanzadas implementadas:
- ✅ Grupos y usuarios con permisos
- ✅ Formulario de contacto con Mailtrap
- ✅ API REST (GET y POST)
- ✅ Consumir API desde la web

¡Disfruta probando todas las funcionalidades!

