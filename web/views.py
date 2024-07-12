from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormForm

# Create your views here.
def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    #all_flans = Flan.objects.all()
    return render(
                    request,
                    'index.html',
                    {
                        'public_flans': public_flans
                    }
                )

def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(
                    request,
                    'welcome.html',
                    {
                        'private_flans': private_flans
                    }
                )

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
     
        if form.is_valid():
            contact_form=ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
        else:  print("Formulario no válido. Errores:", form.errors)
    else:
        form = ContactFormForm()
            
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html', {})
