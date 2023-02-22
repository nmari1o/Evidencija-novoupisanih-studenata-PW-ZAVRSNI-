import factory
from factory.django import DjangoModelFactory
from main.models import *
from factory import fuzzy
from faker import Faker 
fake=Faker()

class MjestoFactory(DjangoModelFactory):
    class Meta:
        model=Mjesto

    postanski_broj=factory.fuzzy.FuzzyInteger(10000,99999)
    naziv_mjesta=factory.Faker("city")

class SveucilisteFactory(DjangoModelFactory):
    class Meta:
        model=Sveuciliste

    naziv_sveucilista=factory.LazyAttribute(lambda o: f"University of {fake.city()}")
    sveuciliste_postanski_broj=factory.Iterator(Mjesto.objects.all())

class FakultetFactory(DjangoModelFactory):
    class Meta:
        model=Fakultet

    fakultet=factory.LazyAttribute(lambda o: f"{fake.city()} College")      
    fakultet_sveuciliste=factory.Iterator(Sveuciliste.objects.all())

class SmjerFactory(DjangoModelFactory):
    class Meta:
        model=Smjer

    naziv_smjera=factory.Faker("sentence", nb_words=5)

    @factory.post_generation
    def fakultet(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return fakultet

        if extracted:
            # A list of groups were passed in, use them
            for fakultet in extracted:
                self.fakultet.add(fakultet)
                return fakultet     

        else:
            fakultet=FakultetFactory()
            self.fakultet.add(fakultet)
            return fakultet  

        fakultet.save() 

        return fakultet            
    faks=fakultet
        


            
class SrednjaSkolaFactory(DjangoModelFactory):
    class Meta:
        model=SrednjaSkola

    naziv_srednje=factory.LazyAttribute(lambda o: f"{fake.city()} High School")
    srednja_postanski_broj=factory.Iterator(Mjesto.objects.all())

class MaturantFactory(DjangoModelFactory):
    class Meta:
        model=Maturant

    ime_maturanta=factory.Faker("first_name")
    prezime_maturanta=factory.Faker("last_name")
    upisni_broj=factory.fuzzy.FuzzyInteger(100000,999999)
    email_maturanta= factory.Faker("email")
    maturant_smjer=factory.Iterator(Smjer.objects.all())
    maturant_fakultet=factory.Iterator(Fakultet.objects.all())
    maturant_postanski_broj=factory.Iterator(Mjesto.objects.all())
    maturant_srednja_skola=factory.Iterator(SrednjaSkola.objects.all())
    maturant_datum_upisa=factory.Faker("date_time")     

class StudentFactory(DjangoModelFactory):
    class Meta:
        model=Student

    ime_studenta=factory.Faker("first_name")
    prezime_studenta=factory.Faker("last_name")
    jmbag_studenta= factory.fuzzy.FuzzyInteger(1000000000,9999999999)
    email_studenta=factory.Faker("email")
    student_smjer=factory.Iterator(Smjer.objects.all())
    student_fakultet=factory.Iterator(Fakultet.objects.all())
    student_postanski_broj=factory.Iterator(Mjesto.objects.all())
    student_datum_upisa=factory.Faker("date_time") 
 

