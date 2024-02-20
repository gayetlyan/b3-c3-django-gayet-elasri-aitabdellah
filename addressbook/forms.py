from django import forms
from .models import Contact
from .models import Site


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url', 'username', 'password']