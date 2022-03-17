from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .models import *
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

def listarAutor (request):
     autorL=autor.objects.all()#.filter(estado=true) o .filter(nombre='juan')
     #filter devuelve datos filtrados
     return render(request,'libros\listarAutor.html',{'autorL':autorL})
 
def editarAutor (request,id):
    autorForm=None
    error=None
    try:
        autorE=autor.objects.get(id=id)# solo trae un objeto filtrado por la variable que le pasamos
        if request.method=='GET':
            autorForm=AutorForm(instance=autorE)
        else:
            autorForm=AutorForm(request.POST, instance=autorE)
            if autorForm.is_valid(): # valida el formulario
                autorForm.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error=e
        
    return render(request,'libros\crearA.html',{'autorForm':autorForm,'error':error})

def eliminarAutor (request,id):
    autors=autor.objects.get(id=id)
    if request.method=='POST':
        #eliminacion logica
        #autor.estado=false
        #autor.save() el estado es un valor del modelo que aun no e creado
        autors.delete()
        return redirect('libro:listarA')
    return render(request,'libros\eliminarAutor.html',{'autor':autors})

"""
def crearAutor(request):
    if request.method == 'POST':
        nom=request.POST.get('nombre')#los valores finales son los nombres asignados en el html
        apell=request.POST.get('apellido')
        nacionali=request.POST.get('nacionalidad')
        descrip=request.POST.get('descripcion')
        autors=autor(nombre=nom, apellido=apell,nacionalidad=nacionali, descrip=descripcion)
        #nombres de como aparece en el modelo mas el valor obtenido
        autors.save()
        return redirect('index')
        
        
    return render(request,'libros\crearA.html',{'autorForm':autorForm}) 
    
    #tambien se puede solo dejar el forms y guardar directamente sin modificar el codigo de arriba
    
    

"""