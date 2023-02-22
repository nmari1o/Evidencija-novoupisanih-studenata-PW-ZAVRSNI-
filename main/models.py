from django.db import models
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone


# Create your models here.

class Mjesto(models.Model):
    postanski_broj = models.IntegerField(default=10000, help_text='value 10 000 to 99 999', validators=[MaxValueValidator(99999),
            MinValueValidator(10000)], unique=True)
    naziv_mjesta=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.naziv_mjesta}, {self.postanski_broj}'

class Sveuciliste(models.Model):
    naziv_sveucilista=models.CharField(max_length=50)
    sveuciliste_postanski_broj=models.OneToOneField(Mjesto, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.naziv_sveucilista

class Fakultet(models.Model):
    fakultet_sveuciliste=models.ForeignKey(Sveuciliste, on_delete=models.CASCADE)
    fakultet=models.CharField(max_length=70)

    def __str__(self):
        return self.fakultet

class Smjer(models.Model):
    naziv_smjera=models.CharField(max_length=70)
    fakultet=models.ManyToManyField(Fakultet)

    def __str__(self):
        return self.naziv_smjera

class SrednjaSkola(models.Model):
    naziv_srednje=models.CharField(max_length=100)
    srednja_postanski_broj=models.ForeignKey(Mjesto, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_srednje

class Maturant(models.Model):
    ime_maturanta=models.CharField(max_length=20)
    prezime_maturanta=models.CharField(max_length=30)
    upisni_broj=models.IntegerField(default=10000, help_text='value 10 000 to 99 999', validators=[MaxValueValidator(99999),
            MinValueValidator(10000)], unique=True)
    email_maturanta=models.EmailField(max_length=70,unique=True)
    maturant_smjer=models.ForeignKey(Smjer, on_delete=models.CASCADE)
    maturant_fakultet=models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    maturant_postanski_broj=models.ForeignKey(Mjesto, on_delete=models.CASCADE)
    maturant_srednja_skola=models.ForeignKey(SrednjaSkola, on_delete=models.CASCADE)
    maturant_datum_upisa=models.DateField(default=timezone.now)

    def __str__(self):
        return self.ime_maturanta

def validate_10_digits(value):
    if len(str(value))!=10:
        raise ValidationError('Vrijednost JMBAG-a mora sadržavati točno 10 znamenki.')        

class Student(models.Model):
    ime_studenta=models.CharField(max_length=20)
    prezime_studenta=models.CharField(max_length=30)
    jmbag_studenta= models.IntegerField(validators=[validate_10_digits], unique=True)
    email_studenta=models.EmailField(max_length=70,unique=True)
    student_smjer=models.ForeignKey(Smjer, on_delete=models.CASCADE)
    student_fakultet=models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    student_postanski_broj=models.ForeignKey(Mjesto, on_delete=models.CASCADE)
    student_datum_upisa=models.DateField(default=timezone.now)

    def __str__(self):
        return self.ime_studenta
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # Add other fields here


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    # Add other fields here
    
    class Meta:
        model = User
        fields = ['username', 'name', 'address', 'password1', 'password2']




