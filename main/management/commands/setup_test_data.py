import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_MJESTO = 100
NUM_SVEUCILISTE = 100
NUM_SREDNJA=100
NUM_FAKULTET=10
NUM_MATURANT=100
NUM_STUDENT=100
NUM_SMJER=100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Mjesto, Sveuciliste, SrednjaSkola, Fakultet, Smjer, Student, Maturant]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_MJESTO):
            mjesto = MjestoFactory()

        for _ in range(NUM_SVEUCILISTE):
            sveuciliste = SveucilisteFactory()

        for _ in range(NUM_SREDNJA):
            srednja = SrednjaSkolaFactory()  

        for _ in range(NUM_FAKULTET):
            fakultet=FakultetFactory()

        for _ in range(NUM_SMJER):
            smjer=SmjerFactory()    

        for _ in range(NUM_STUDENT):
            student = StudentFactory()     

        for _ in range(NUM_MATURANT):
            maturant = MaturantFactory()         
        
       