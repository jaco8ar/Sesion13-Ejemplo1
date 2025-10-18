from django.shortcuts import render, get_object_or_404
from app_libro.models import Libro

def index(request):
    """Vista de listado de libros"""
    libros = Libro.objects.all()
    return render(request, "app_ejemplo01/index.html", {"libros": libros})

def detalle(request, pk):
    """Vista de detalle de un libro específico"""
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "app_ejemplo01/detalle.html", {"libro": libro})
