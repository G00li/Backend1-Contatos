from django.shortcuts import render
from contact.models import Contact


# Create your views here.

def index(request): #Função para renderizar o index.html 

    contacts = Contact.objects.filter().order_by('-id') #organizao o ultimo adicionado sendo o primeiro a ser exibido (pilha e fila)

    context = {
        'contacts' : contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
def contact(request,contact_id): 

    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact' : single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )