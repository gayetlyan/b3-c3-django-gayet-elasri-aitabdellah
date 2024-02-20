from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    generate_password = models.BooleanField(default=False)


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url', 'username', 'password']


class Password(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    generate_password = models.BooleanField(default=False)


    def __str__(self):
        return self.name


