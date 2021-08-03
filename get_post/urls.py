from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('primeraApp.urls')),
    path('aleatoria/' ,include('aleatoria.urls')),
]
