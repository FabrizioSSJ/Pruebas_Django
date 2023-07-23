from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #  path('', views.inicio, name="inicio"),
    #  path('sobremi/', views.sobre_mi, name="sobremi"),
    #  path('sobremi/<str:msj>/', views.hola, name="hola"),
    path('inicio', views.inicio, name="inicio"),
    path('puntos', views.puntos, name="puntos"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("crear", views.crear, name="crear"),
    path("form", views.form, name="form"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("borrar/<int:id>", views.borrar, name="borrar")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
