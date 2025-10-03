from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class tabelaadmin(admin.ModelAdmin):
    list_display=('nome','email')
    
    search_fields=('nome','email')
