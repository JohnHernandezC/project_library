from django.shortcuts import redirect, render

from .forms import AutorForm

def inicio (request):
    return render(request,'libros\libros.html')


def crearAutor(request):
    if request.method == 'POST':
        autorForm=AutorForm(request.POST)#recibe datos almacenados en la peticion POST
        if autorForm.is_valid(): # valida el formulario
            autorForm.save()
            return redirect('index')
        
    else: 
        autorForm=AutorForm()
        
    return render(request,'libros\crearA.html',{'autorForm':autorForm})