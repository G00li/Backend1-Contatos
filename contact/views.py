from django.shortcuts import render

# Create your views here.

def index(request): #Função para renderizar o index.html 
    return render(
        request,
        'contact/index.html'
    )