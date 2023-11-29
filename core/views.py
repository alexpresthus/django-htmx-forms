from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def index(request):
    context = {'form': ContactForm, 'contacts': Contact.objects.all()}
    return render(request, 'index.html', context)

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save()
            context = {'contact': contact}
            return render(request, 'partials/contact.html', context)
    
    if request.method == 'GET':
        return render(request, 'partials/form.html', { 'form': ContactForm })