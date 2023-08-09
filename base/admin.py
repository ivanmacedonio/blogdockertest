from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

class CategoryResource(resources.ModelResource): #agrega boton de exportar o importar data al formato elegido
    class Meta:
        model  =Category

class PostResource(resources.ModelResource): #agrega boton de exportar o importar data al formato elegido
    class Meta:
        model  =Post

class AuthorResource(resources.ModelResource): #agrega boton de exportar o importar data al formato elegido
    class Meta:
        model  =Author


class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin): #addons para el admin
    search_fields = ['name'] #agrega una barra de busqueda al modelo donde filtramos por name
    list_display = ('name',) #elegimos que campos de la instancia mostrar en el admin. Es modificable cambiando el nombre desde el campo del modelo
    resource_class = CategoryResource

class AuthorAdmin(admin.ModelAdmin): 
    search_fields = ['name']
    list_display = ('name', 'description',)
    resource_class = AuthorResource

class PostAdmin(admin.ModelAdmin): 
    search_fields = ['title', 'author']
    list_display = ('title', 'author',)
    resource_class = PostResource



admin.site.register(Category, CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Web)
admin.site.register(ContactUs)
admin.site.register(Suscriptor)
