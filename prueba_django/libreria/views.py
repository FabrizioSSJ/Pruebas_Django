from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import punto
from .form import punto_form
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
    formulario= punto_form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect(puntos)
    return render(request, "puntos/crear.html", {'formulario': formulario})
def form(request):
    return render(request, "puntos/form.html")
def editar(request, id):
    puntos=punto.objects.get(id=id)
    formulario= punto_form(request.POST or None, request.FILES or None, instance=puntos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('puntos')
    return render(request, "puntos/editar.html", {'formulario': formulario})
def borrar(request, id):
    puntos=punto.objects.get(id=id)
    puntos.delete()
    return redirect("puntos")