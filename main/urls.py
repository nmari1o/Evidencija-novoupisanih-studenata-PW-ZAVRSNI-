from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('pocetna/', views.main, name='main'),
    path('mjesta/', views.mjesto_list, name="mjesto"),
    path('sveucilista/', views.sveuciliste_list, name="sveuciliste"),
    path('srednja/', views.srednjaskola_list, name="srednja"),
    path('fakultet/', views.fakultet_list, name="fakultet"),
    path('smjer/', views.smjer_list, name="smjer"),
    path('maturant/',views.maturant_list, name="maturant"),
    path('student/',views.student_list, name='student'),
    path('', LoginRegisterView.as_view(), name='login_register'),


    path('student_form/', views.student_form, name="student_form"),
    path('maturant_form/', views.maturant_form, name="maturant_form"),
    path('sveuciliste_form/', views.sveuciliste_form, name="sveuciliste_form"),
    path('mjesto_form/', views.mjesto_form, name="mjesto_form"),
    path('fakultet_form/', views.fakultet_form, name="fakultet_form"),
    path('smjer_form/', views.smjer_form, name="smjer_form"),
    path('srednjaskola_form/', views.srednjaskola_form, name="srednjaskola_form"),







    path('student/<int:jmbag_studenta>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('maturant/<int:upisni_broj>/update/', views.MaturantUpdateView.as_view(), name='maturant_update'),
 


    path('fakultet/<str:fakultet>/update', views.FakultetUpdateView.as_view(), name='fakultet_update'),
    path('smjer/<str:naziv_smjera>/update', views.SmjerUpdateView.as_view(), name='smjer_update'),

    path('srednja/<str:naziv_srednje>/update', views.SrednjaUpdateView.as_view(), name='srednja_update'),
    path('mjesto/<str:naziv_mjesta>/update', views.MjestoUpdateView.as_view(), name='mjesto_update'),

    path('sveuciliste/<str:naziv_sveucilista>/update', views.SveucilisteUpdateView.as_view(), name='sveuciliste_update'),



    path('student/<int:jmbag_studenta>/delete', views.StudentDeleteView.as_view(), name='student_delete'),
    path('maturant/<int:upisni_broj>/delete', views.MaturantDeleteView.as_view(), name='maturant_delete'),
    path('mjesto/<int:postanski_broj>/delete', views.MjestoDeleteView.as_view(), name='mjesto_delete'),
    path('fakultet/<str:fakultet>/delete', views.FakultetDeleteView.as_view(), name='fakultet_delete'),
    path('sveuciliste/<str:naziv_sveucilista>/delete', views.SveucilisteDeleteView.as_view(), name='sveuciliste_delete'),
    path('smjer/<str:naziv_smjera>/delete', views.SmjerDeleteView.as_view(), name='smjer_delete'),
    path('srednja/<str:naziv_srednje>/delete', views.SrednjaDeleteView.as_view(), name='srednjaskola_delete'),

    path('logout/', LogoutView.as_view(next_page='/login'), name='logout'),





]
