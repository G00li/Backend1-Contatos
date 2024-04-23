from django.urls import path
from contact import views

app_name = 'contact' #name space para nao ter conflitos entre os nomes !mente explodiu!


urlpatterns = [
    path("", views.index, name='index'),
    
    ]
