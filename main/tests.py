from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
import urllib.parse
from .models import *

from . import views

class UrlDelete(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mjesto = Mjesto.objects.create(postanski_broj=1887, naziv_mjesta='Tiffanyport')
        cls.srednja_skola = SrednjaSkola.objects.create(naziv_srednje='Juliebury High School', srednja_postanski_broj=cls.mjesto)

    def test_mjesto_delete_url_resolves(self):
        postanski_broj = 1887
        url = reverse('main:mjesto_delete', kwargs={'postanski_broj': postanski_broj})
        self.assertEqual(url, f'/mjesto/{postanski_broj}/delete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)     


    def test_srednja_delete_url_resolves(self):
        naziv_srednje = 'Juliebury High School'
        url = reverse('main:srednjaskola_delete', kwargs={'naziv_srednje': naziv_srednje})
        expected_url = f'/srednja/{naziv_srednje.replace(" ", "%20")}/delete'
        self.assertEqual(url, expected_url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)       


class UrlUpdate(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mjesto = Mjesto.objects.create(postanski_broj=1887, naziv_mjesta='Tiffanyport')
        cls.srednja_skola = SrednjaSkola.objects.create(naziv_srednje='Juliebury High School', srednja_postanski_broj=cls.mjesto)
        cls.sveuicliste=Sveuciliste.objects.create(naziv_sveucilista="University of Zagreb", sveuciliste_postanski_broj=cls.mjesto)
        cls.fakultet = Fakultet.objects.create(fakultet='Fakultet racunarstva', fakultet_sveuciliste=cls.sveuicliste)

    def test_srednja_update_url_resolves(self):
        naziv_srednje = 'Juliebury High School'
        url = reverse('main:srednjaskola_delete', kwargs={'naziv_srednje': naziv_srednje})
        expected_url = f'/srednja/{naziv_srednje.replace(" ", "%20")}/delete'
        self.assertEqual(url, expected_url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)    

    def test_fakultet_update_url_resolves(self):
        fakultet = 'Fakultet racunarstva'
        url = reverse('main:fakultet_update', kwargs={'fakultet': fakultet})
        expected_url=f'/fakultet/{fakultet.replace(" ", "%20")}/update'
        self.assertEqual(url, expected_url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)    



class UrlsTest(TestCase):
      

    def test_main_url_resolves(self):
        url = reverse('main:main')
        self.assertEqual(url, '/pocetna/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_mjesto_url_resolves(self):
        url = reverse('main:mjesto')
        self.assertEqual(url, '/mjesta/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_sveuciliste_url_resolves(self):
        url = reverse('main:sveuciliste')
        self.assertEqual(url, '/sveucilista/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_srednjaskola_url_resolves(self):
        url = reverse('main:srednja')
        self.assertEqual(url, '/srednja/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_fakultet_url_resolves(self):
        url = reverse('main:fakultet')
        self.assertEqual(url, '/fakultet/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_smjer_url_resolves(self):
        url = reverse('main:smjer')
        self.assertEqual(url, '/smjer/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_maturant_url_resolves(self):
        url = reverse('main:maturant')
        self.assertEqual(url, '/maturant/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_student_url_resolves(self):
        url = reverse('main:student')
        self.assertEqual(url, '/student/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_login_register_url_resolves(self):
        url = reverse('main:login_register')
        self.assertEqual(url, '/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_student_form_url_resolves(self):
        url = reverse('main:student_form')
        self.assertEqual(url, '/student_form/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_maturant_form_url_resolves(self):
        url = reverse('main:maturant_form')
        self.assertEqual(url, '/maturant_form/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_sveuciliste_form_url_resolves(self):
        url = reverse('main:sveuciliste_form')
        self.assertEqual(url, '/sveuciliste_form/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_mjesto_form_url_resolves(self):
        url = reverse('main:mjesto_form')
        self.assertEqual(url, '/mjesto_form/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_fakultet_form_url_resolves(self):
        url = reverse('main:fakultet_form')
        self.assertEqual(url, '/fakultet_form/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

 





class SveucilisteModelTestCase(TestCase):
    def test_sveuciliste_str(self):
        mjesto = Mjesto.objects.create(postanski_broj=10000, naziv_mjesta="Test")
        sveuciliste = Sveuciliste.objects.create(naziv_sveucilista="Test Sveučilište", sveuciliste_postanski_broj=mjesto)
        self.assertEqual(str(sveuciliste), "Test Sveučilište")

class FakultetModelTestCase(TestCase):
    def test_fakultet_str(self):
        mjesto = Mjesto.objects.create(postanski_broj=10000, naziv_mjesta="Test")
        sveuciliste = Sveuciliste.objects.create(naziv_sveucilista="Test Sveučilište", sveuciliste_postanski_broj=mjesto)
        fakultet = Fakultet.objects.create(fakultet_sveuciliste=sveuciliste, fakultet="Test Fakultet")
        self.assertEqual(str(fakultet), "Test Fakultet")

class SmjerModelTestCase(TestCase):
    def test_smjer_str(self):
        mjesto = Mjesto.objects.create(postanski_broj=10000, naziv_mjesta="Test")
        sveuciliste = Sveuciliste.objects.create(naziv_sveucilista="Test Sveučilište", sveuciliste_postanski_broj=mjesto)
        fakultet = Fakultet.objects.create(fakultet_sveuciliste=sveuciliste, fakultet="Test Fakultet")
        smjer = Smjer.objects.create(naziv_smjera="Test Smjer")
        smjer.fakultet.add(fakultet)
        self.assertEqual(str(smjer), "Test Smjer")
   