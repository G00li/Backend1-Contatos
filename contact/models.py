from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50) #criando uma tabela de categoria 
   
    def __str__(self) -> str: #Exbibe apenas o nome da categoria
        return f'{self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 50, blank=True) #o blank = True faz com que fique opcional 
    phone = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 254, blank=True)
    created_date = models.DateTimeField(default=timezone.now) #Registra a hora em que o contato foi criado
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank= True, null=True) #quando a categoria Category for excluida, nada irá acontecer 
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True)

    def __str__(self) -> str: #Exbibe o primeiro e o ultimo nome na lista 
        return f'{self.first_name} {self.last_name}'
