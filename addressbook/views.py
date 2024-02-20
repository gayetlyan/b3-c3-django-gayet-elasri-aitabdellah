# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from .models import Site
from .forms import SiteForm
import csv
from django.http import HttpResponse
from .models import Password




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


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('site_list') 
    else:
        form = SiteForm()
    return render(request, 'addressbook/add_site.html', {'form': form})


def export_passwords_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Password'])  

    passwords = Password.objects.all()  

    for password in passwords:
        writer.writerow([password.username, password.password])  

    return response