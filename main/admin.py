from django.contrib import admin
from main.models import Mjesto, Sveuciliste, Fakultet, Smjer, SrednjaSkola, Maturant, Student
# Register your models here.

models_list = [Mjesto, Sveuciliste, Fakultet, Smjer, SrednjaSkola, Maturant, Student]

admin.site.register(models_list)