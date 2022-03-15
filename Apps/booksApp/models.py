from django.db import models


class autor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=100)
    descripcion=models.TextField()
    create=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural ='Autores'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre
        
class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    fechaLanzamiento=models.DateField(auto_now_add=True)
    #autorId=models.OneToOneField(autor,on_delete=models.CASCADE)#relacion de 1 a uno
    autorId=models.ForeignKey(autor,on_delete=models.CASCADE)#relacion de 1 a muchos
    #autorId=models.ManyToManyField(autor)#relacion de muchos a muchos
    create=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'libro'
        verbose_name_plural ='libros'
        ordering = ['titulo']
        
    def __str__(self):
        return self.titulo
    