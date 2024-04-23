from django.contrib import admin
from contact import models


# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'category', 'phone', #Cria colunas no admin para exibir o contato
    ordering = 'first_name', #Ordena de forma alfabética
    # list_filter = 'created_date' #Cria um campo de filtro por data
    search_fields = 'id', 'first_name', 'last_name', 'phone',

    #Dividindo os contatos por páginas 
    list_per_page = 1 # Resolve o problema de quando temos muitos dados. Ele divide em páginas
    list_per_page = 10 #Contatos por páginas 
    list_max_show_all = 200

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name', #Ordena de forma alfabética
