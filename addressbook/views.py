# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from .models import Site


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'addressbook/contact_list.html', {'contacts': contacts})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'addressbook/contact_form.html', {'form': form})

@login_required
def contact_update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'addressbook/contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('contact_list')



def site_list(request):
    sites = Site.objects.filter(user=request.user)
    return render(request, 'addressbook/site_list.html', {'sites': sites})
