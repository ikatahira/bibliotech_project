from django.contrib import admin
from .models import Genero, Editora, Autor, Livro
# Register your models here.
admin.site.register(Genero)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
