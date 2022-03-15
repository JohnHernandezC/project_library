from django.contrib import admin
from .models import *

class autorAdmin(admin.ModelAdmin):
    #readonly_fields=('create','update')
    list_display = ('id','nombre')
    search_fields = ('nombre','apellido')
    
    
class libroAdmin(admin.ModelAdmin):
    #readonly_fields=('create','update')
    list_display = ('id','titulo')
    search_fields = ('titulo',)
    
    
    

admin.site.register(autor,autorAdmin)
admin.site.register(Libro,libroAdmin)
