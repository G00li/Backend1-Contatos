from django.shortcuts import redirect, render
from contact.models import Contact
from django.db.models import Q


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

def search(request):
    search_value = request.GET.get('q')

    if search_value == '':
        return redirect('contact:index') #Verifica se o valor foi enviado, se nao retorna para pagina incial 

    contacts = Contact.objects.filter(
            Q(first_name__icontains=search_value)|
            Q(last_name__icontains=search_value)|
            Q(phone__icontains=search_value)|
            Q(email__icontains=search_value)
        ).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )
