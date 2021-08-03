from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    # path('get_o_post/', views.get_o_post),
    path('formulario/', views.formulario),
    path('registrarUsuario/', views.registrarUsuario),
    path('usuarioRegistrado/',views.usuarioRegistrado),
    path('mostrarUsuario/' , views.mostrarUsuario),
    path('terminarSesion/' , views.terminarSesion),
]
