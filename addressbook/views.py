# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from .models import Site
from .forms import SiteForm
import csv
from django.http import HttpResponse
from .models import Password
from .utils import generate_random_password
from django.shortcuts import render, redirect, get_object_or_404



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


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('site_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')




def import_passwords_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if csv_file.name.endswith('.csv'):
            reader = csv.reader(csv_file)
            next(reader)  
            for row in reader:
                username, password = row
                Password.objects.create(username=username, password=password)
            return HttpResponseRedirect('/passwords/') 
        else:
            return render(request, 'invalid_file_format.html')  
    return render(request, 'addressbook/import_passwords.html')  


def update_site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list') 
    else:
        form = SiteForm(instance=site)
    return render(request, 'addressbook/update_site.html', {'form': form})






def supprimer_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)

    site.delete()

    return redirect('site_list')







