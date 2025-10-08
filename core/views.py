from django.shortcuts import render

def home(request):
    juegos = [
        {"titulo": "Admin Abuse", "descripcion": "Explora los eventos más caóticos.", "url": "https://static.beebom.com/wp-content/uploads/2025/08/Asteroid-Event.jpg?w=1000"},
        {"titulo": "Power-Ups", "descripcion": "Consigue mejoras durante la partida.", "url": "https://techwiser.com/wp-content/uploads/2025/08/How-to-Get-Brainrot-Gods-in-Steal-a-Brainrot-Roblox.webp"},
        {"titulo": "Los Secretos", "descripcion": "Consigue brainrots unicos.", "url": "https://i.pinimg.com/originals/19/bf/14/19bf14e4e5e6d105bbeb7307a1874200.webp"},
    ]
    comentarios = [
        {"nombre": "laratitapeke", "texto": "DEVUELVANME MI VACA SATURNO SATURNITAAAA"},
        {"nombre": "NoobMaster", "texto": "Todos quieren mi udindindun."},
    ]
    contexto = {
        "juegos": juegos,
        "comentarios": comentarios,
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_title": "Roba un Brainrot - Home",
    }
    return render(request, "core/home.html", contexto)

def about(request):
    contexto = {
        "mision": "Hacer que todos pierdan el control en un ambiente brainrot divertido.",
        "vision": "Convertirse en el juego más caótico de Roblox.",
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_title": "Roba un Brainrot - Quiénes Somos",
    }
    return render(request, "core/about.html", contexto)

def faq(request):
    faqs = [
        {"q": "¿Los tours incluyen seguro?", "a": "Sí, todos nuestros tours incluyen un seguro básico."},
        {"q": "¿Necesito experiencia previa?", "a": "No necesariamente. Indicamos la dificultad de cada tour."},
        {"q": "¿Qué debo llevar?", "a": "Ropa adecuada, agua, bloqueador y documento de identidad."},
    ]
    contexto = {
        "faqs": faqs,
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_title": "Roba un Brainrot - Preguntas Frecuentes",
    }
    return render(request, "core/faq.html", contexto)

def gallery(request):
    imagenes = [
        {"nombre": "Tralalero Tralala", "url": "https://elmercurio.com.mx/wp-content/uploads/2025/05/tralalero-tralala.jpg"},
        {"nombre": "Tung Tung Tung Sahur", "url": "https://upload.wikimedia.org/wikipedia/commons/1/12/Full_image_of_Tung_Tung_Tung_Sahur.png"},
        {"nombre": "Bombardiro crocodrillo", "url": "https://brushmeworld.com/cdn/shop/files/2_4004c186-b51a-4488-8125-7de4fd984528.jpg?v=1746642987"},
        {"nombre": "Vaca saturno Saturnita", "url": "https://makerworld.bblmw.com/makerworld/model/DSM00000001471545/design/2025-05-31_1d2894587342f8.jpg?x-oss-process=image/resize,w_1000/format,webp"},
        {"nombre": "Bombini Gusini", "url": "https://italianbrainrotcard.com/cdn/shop/articles/Bombini_Gusini.jpg?v=1746634062"},
        {"nombre": "bobrito Bandito", "url": "https://static.wikitide.net/italianbrainrotwiki/thumb/9/90/Bober_Bandito.jpg/300px-Bober_Bandito.jpg"},
    ]
    contexto = {
        "imagenes": imagenes,
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_title": "Roba un Brainrot - Galería",
    }
    return render(request, "core/gallery.html", contexto)