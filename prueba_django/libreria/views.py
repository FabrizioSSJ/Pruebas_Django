from django.shortcuts import render
from django.http import HttpResponse
from .models import punto
# Create your views here.

# def inicio(request):
#      return HttpResponse("<h1>Bienvenido al punto inteligente</>")
# def sobre_mi(request):
#      return HttpResponse("Soy Fabrizio")
# def hola(request, msj):
#      return HttpResponse(f"<h1>{hola}</h1>") #Ruteo dinamico

def inicio(request):
    return render(request, "puntos/inicio.html")
def puntos(request):
    puntos = punto.objects.all()
    return render(request, "puntos/index.html", {'puntos': puntos})
def nosotros(request):
    return render(request, "puntos/nosotros.html")
def crear(request):
    return render(request, "puntos/crear.html")
def form(request):
    return render(request, "puntos/form.html")
def editar(request):
    return render(request, "puntos/editar.html")
def borrar(request):
    return render(request, "puntos/borrar.html")