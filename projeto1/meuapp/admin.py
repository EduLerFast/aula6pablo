from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class tabela_de_clientes(admin.ModelAdmin):
    list_display=('nome','email')
    
    search_fields=('nome','email')
