from django.urls import path
from .views import *

urlpatterns =[
    path('crear/',crearAutor,name='crearA'),
    path('listar/',listarAutor,name='listarA'),
    path('editar/<int:id>',editarAutor,name='editarA'),
    path('eliminar/<int:id>',eliminarAutor,name='eliminarA'),
    
]