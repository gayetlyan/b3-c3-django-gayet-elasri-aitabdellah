from django import forms
from .models import Contact
from .models import Site
from .utils import generate_random_password


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']


class SiteForm(forms.ModelForm):
    generate_password = forms.BooleanField(required=False)

    class Meta:
        model = Site
        fields = ['name', 'url', 'username', 'password', 'generate_password']

    def clean_password(self):
        generate_password = self.cleaned_data.get('generate_password')
        password = self.cleaned_data.get('password')

        if generate_password:
            return generate_random_password()
        else:
            return password