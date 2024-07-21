from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormForm, RegistrationForm

def index(request):
    public_flans = Flan.objects.filter(is_private=False)
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

def login(request):
    return render(request, 'login.html', {})

def logged_out(request):
    return render(request, 'logged_out.html', {})

def signup(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message_to_show = f'User {username} created sucessfully!'
            messages.success(request, message_to_show.format(username))
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', { 'form':form })

def recipe(request):
    categories = ['tradicional', 'innovador', 'sin_azucar']
    selected_category = request.GET.get('category', '')
    flans = Flan.objects.filter(category=selected_category) if selected_category else Flan.objects.all()
    return render(request, 'recipe.html', {'flans': flans, 'categories': categories, 'selected_category': selected_category})

def recipe_detail(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    return render(request, 'recipe_detail.html', {'flan': flan})