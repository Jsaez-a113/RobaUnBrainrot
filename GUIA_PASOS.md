# Guía de Pasos para Ver las Nuevas Funciones

## 📋 Requisitos Previos

1. **Instalar dependencias**:
```bash
pip install django-crispy-forms crispy-bootstrap5
```

2. **Crear y aplicar migraciones**:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Iniciar servidor**:
```bash
python manage.py runserver
```

---

## 🎯 Paso 1: Configurar Datos de Prueba

### 1.1 Acceder al Admin
- URL: `http://127.0.0.1:8000/admin/`
- Usuario: `root`
- Contraseña: `root123`

### 1.2 Crear Categorías
1. Ir a **"Categorías"** → **"Añadir categoría"**
2. Crear al menos 3 categorías:
   - **Categoría 1**: Nombre: "Memes", Slug: "memes"
   - **Categoría 2**: Nombre: "Personajes", Slug: "personajes"
   - **Categoría 3**: Nombre: "Eventos", Slug: "eventos"

### 1.3 Crear Items Brainrot
1. Ir a **"Items Brainrot"** → **"Añadir item brainrot"**
2. Crear 15-20 items con:
   - Nombre y descripción
   - **Subir una imagen** (importante)
   - Asignar diferentes categorías
   - Marcar algunos como **"Destacado"**
   - Guardar

### 1.4 Crear Comentarios (Opcional)
1. Ir a **"Comentarios"** → **"Añadir comentario"**
2. Crear comentarios vinculados a items
3. Marcar algunos como **"Aprobado"**

---

## 🎯 Paso 2: Ver Funcionalidades en el Frontend

### 2.1 Procesador de Contexto (Estadísticas)
**URL**: `http://127.0.0.1:8000/`

**Qué verificar**:
- Ir al **footer** de cualquier página
- Deberías ver:
  - 📦 X Items
  - 🏷️ X Categorías
  - 💬 X Comentarios
  - ⭐ X Destacados

### 2.2 Filtros en Lista de Items
**URL**: `http://127.0.0.1:8000/items/`

**Qué probar**:
1. **Filtro por categoría**:
   - Selecciona una categoría del dropdown
   - Haz clic en "Filtrar"
   - Solo se muestran items de esa categoría

2. **Orden por fecha**:
   - Selecciona "Más recientes" o "Más antiguos"
   - Los items se ordenan según la selección

3. **Solo destacados**:
   - Selecciona "Solo destacados"
   - Solo aparecen items marcados como destacados

4. **Búsqueda**:
   - Escribe texto en el campo "Buscar"
   - Busca por nombre o descripción

5. **Filtros combinados**:
   - Combina categoría + fecha + búsqueda
   - La paginación mantiene los filtros

### 2.3 Detalle de Item con Comentarios
**URL**: `http://127.0.0.1:8000/items/<id>/`

**Qué verificar**:
- Imagen del item
- Nombre y descripción completa
- Badge de categoría (si tiene)
- Badge "⭐ Destacado" (si está marcado)
- **Contador de visitas** (se incrementa cada vez que cargas la página)
- Fechas de creación y actualización
- **Sección de comentarios** (si hay comentarios aprobados)

### 2.4 Formulario de Contacto
**URL**: `http://127.0.0.1:8000/contacto/`

**Qué probar**:
1. Completar el formulario:
   - Nombre
   - Email
   - Asunto
   - Mensaje

2. Enviar el formulario

3. Verificar:
   - Mensaje de éxito aparece
   - El mensaje se guarda en la base de datos

4. En el Admin:
   - Ir a **"Mensajes de Contacto"**
   - Ver el mensaje guardado
   - Marcar como "Leído" si deseas

### 2.5 Error 404 Personalizado
**URLs para probar**:
- `http://127.0.0.1:8000/pagina-inexistente/`
- `http://127.0.0.1:8000/items/999999/` (si no existe ese ID)

**Qué verificar**:
- Página 404 personalizada con diseño
- Mensaje amigable
- Enlaces de navegación (Inicio, Items, Galería)
- No aparece el error por defecto de Django

---

## 🎯 Paso 3: Ver Funcionalidades en el Admin

### 3.1 Admin Personalizado de BrainrotItem
**URL**: `http://127.0.0.1:8000/admin/brainrot/brainrotitem/`

**Funcionalidades a verificar**:

1. **Miniaturas de imágenes**:
   - Columna "Imagen" muestra miniaturas de 50x50px

2. **Edición directa en lista**:
   - Marca/desmarca "Destacado" directamente
   - Cambia el número de "Visitas" directamente

3. **Filtros laterales**:
   - Por categoría
   - Por destacado
   - Por fecha de creación
   - Por fecha de actualización

4. **Búsqueda**:
   - Busca en nombre, descripción y nombre de categoría

5. **Navegación por fecha**:
   - En la parte superior hay un selector de año/mes

6. **Acciones masivas**:
   - Selecciona varios items
   - Elige "Marcar como destacados" o "Quitar marca de destacados"
   - Aplica la acción

7. **Agrupación de campos**:
   - Al editar un item, verás campos agrupados en secciones:
     - Información Básica
     - Imagen
     - Opciones
     - Fechas (colapsable)

### 3.2 Ver Relaciones entre Modelos
**URLs del Admin**:
- `http://127.0.0.1:8000/admin/brainrot/category/`
- `http://127.0.0.1:8000/admin/brainrot/brainrotitem/`
- `http://127.0.0.1:8000/admin/brainrot/comment/`

**Qué verificar**:
- En **Categorías**: columna "Items" muestra cuántos items tiene cada categoría
- En **Items**: puedes ver y filtrar por categoría
- En **Comentarios**: puedes ver a qué item pertenece cada comentario

---

## 🎯 Paso 4: Verificar Todas las Funciones Nuevas

### ✅ Checklist de Funcionalidades

#### Modelos Relacionados
- [ ] Category tiene relación con BrainrotItem
- [ ] Comment tiene relación con BrainrotItem y User
- [ ] Puedo crear categorías y asignarlas a items
- [ ] Puedo crear comentarios vinculados a items

#### Admin Personalizado
- [ ] Veo miniaturas de imágenes en la lista
- [ ] Puedo editar "Destacado" y "Visitas" directamente en la lista
- [ ] Funcionan los filtros laterales
- [ ] Funciona la búsqueda
- [ ] Puedo usar acciones masivas
- [ ] Los campos están agrupados en secciones

#### Error 404
- [ ] La página 404 es personalizada
- [ ] Tiene diseño coherente con el sitio
- [ ] Tiene enlaces de navegación

#### Filtros
- [ ] Filtro por categoría funciona
- [ ] Filtro por fecha funciona
- [ ] Filtro de destacados funciona
- [ ] Búsqueda por texto funciona
- [ ] Los filtros se mantienen en la paginación

#### Procesador de Contexto
- [ ] Veo estadísticas en el footer
- [ ] Las estadísticas son correctas
- [ ] Están disponibles en todas las páginas

#### Formulario de Contacto
- [ ] El formulario se ve bien diseñado
- [ ] Puedo enviar el formulario
- [ ] Aparece mensaje de éxito
- [ ] El mensaje se guarda en la base de datos

#### Apps Separadas
- [ ] Core tiene sus propias URLs
- [ ] Brainrot tiene sus propias URLs (`brainrot/urls.py`)
- [ ] Contact tiene sus propias URLs (`contact/urls.py`)
- [ ] Todas están incluidas en el archivo principal de URLs

---

## 🐛 Solución de Problemas

### Si las imágenes no se muestran:
1. Verifica que `Pillow` esté instalado: `pip install Pillow`
2. Verifica que las migraciones estén aplicadas
3. Asegúrate de que el servidor esté corriendo con `DEBUG=True`

### Si el formulario de contacto no funciona:
1. Verifica que `django-crispy-forms` y `crispy-bootstrap5` estén instalados
2. Verifica que `CRISPY_TEMPLATE_PACK = "bootstrap5"` esté en settings.py

### Si no ves las estadísticas:
1. Verifica que el procesador de contexto esté en `TEMPLATES['OPTIONS']['context_processors']`
2. Verifica que hay datos en la base de datos (items, categorías, etc.)

### Si el 404 no se muestra:
1. Asegúrate de que `handler404 = 'core.views.custom_404'` esté en settings.py
2. Verifica que el template `core/templates/core/404.html` exista

---

## 📝 Notas Importantes

- **Paginación**: Muestra 10 items por página
- **Comentarios**: Solo se muestran los comentarios marcados como "Aprobado"
- **Visitas**: Se incrementan cada vez que se carga la página de detalle
- **Destacados**: Se pueden marcar múltiples items como destacados

---

## 🎉 ¡Listo!

Ahora deberías poder ver y probar todas las nuevas funcionalidades implementadas. Si encuentras algún problema, revisa la sección de "Solución de Problemas" o verifica que todos los pasos se hayan ejecutado correctamente.

