from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, DeleteView, UpdateView
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@login_required
def student_form(request):
    form=StudentForm
    if request.method=="POST":
        print(request.POST)
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/student')    
    context={'form':form}
    return render(request, 'student_form.html', context)

@login_required
def maturant_form(request):
    form=MaturantForm
    if request.method=="POST":
        print(request.POST)
        form=MaturantForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/maturant')    
    context={'form':form}
    return render(request, 'maturant_form.html', context)        


@login_required
def mjesto_form(request):
    form=MjestoForm
    if request.method=="POST":
        print(request.POST)
        form=MjestoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/mjesta')    
    context={'form':form}
    return render(request, 'mjesto_form.html', context)  


@login_required
def sveuciliste_form(request):
    form=SveucilisteForm
    if request.method=="POST":
        print(request.POST)
        form=SveucilisteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sveucilista')    
    context={'form':form}
    return render(request, 'sveuciliste_form.html', context) 


@login_required
def fakultet_form(request):
    form=FakultetForm
    if request.method=="POST":
        print(request.POST)
        form=FakultetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/fakultet')    
    context={'form':form}
    return render(request, 'fakultet_form.html', context) 

@login_required
def smjer_form(request):
    form=SmjerForm
    if request.method=="POST":
        print(request.POST)
        form=SmjerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/smjer')    
    context={'form':form}
    return render(request, 'smjer_form.html', context) 

@login_required
def srednjaskola_form(request):
    form=SrednjaForm
    if request.method=="POST":
        print(request.POST)
        form=SrednjaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/srednja')    
    context={'form':form}
    return render(request, 'srednjaskola_form.html', context) 


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_update.html'
    success_url = reverse_lazy('main:student')

    def get_object(self, queryset=None):
        jmbag_studenta = self.kwargs.get('jmbag_studenta')
        return Student.objects.get(jmbag_studenta=jmbag_studenta)


@method_decorator(login_required, name='dispatch')
class MaturantUpdateView(UpdateView):
    model=Maturant
    form_class=MaturantForm
    template_name='maturant_update.html'
    success_url = reverse_lazy('main:maturant')

    def get_object(self, queryset=None):
        upisni_broj=self.kwargs.get('upisni_broj')
        return Maturant.objects.get(upisni_broj=upisni_broj)

@method_decorator(login_required, name='dispatch')    
class FakultetUpdateView(UpdateView):
    model=Fakultet
    form_class=FakultetForm
    template_name='fakultet_update.html'
    success_url = reverse_lazy('main:fakultet')

    def get_object(self, queryset=None):
        fakultet=self.kwargs.get('fakultet')
        return Fakultet.objects.get(fakultet=fakultet)    


@method_decorator(login_required, name='dispatch')
class SmjerUpdateView(UpdateView):
    model=Smjer
    form_class=SmjerForm
    template_name='smjer_update.html'
    success_url=reverse_lazy('main:smjer')

    def get_object(self, queryset=None):
        naziv_smjera=self.kwargs.get('naziv_smjera')
        return Smjer.objects.get(naziv_smjera=naziv_smjera)
    

@method_decorator(login_required, name='dispatch')
class SrednjaUpdateView(UpdateView):
    model = SrednjaSkola    
    form_class = SrednjaForm
    template_name = 'srednja_update.html'
    success_url = reverse_lazy('main:srednja')

    def get_object(self, queryset=None):
        naziv_srednje = self.kwargs.get('naziv_srednje')
        return SrednjaSkola.objects.get(naziv_srednje=naziv_srednje)


@method_decorator(login_required, name='dispatch')
class MjestoUpdateView(UpdateView):
    model=SrednjaSkola
    form_class=MjestoForm
    template_name='mjesto_update.html'
    success_url=reverse_lazy('main:mjesto')

    def get_object(self, queryset=None):
        naziv_mjesta=self.kwargs.get('naziv_mjesta')
        return Mjesto.objects.get(naziv_mjesta=naziv_mjesta)    

@method_decorator(login_required, name='dispatch')
class SveucilisteUpdateView(UpdateView):
    model=Sveuciliste
    form_class=SveucilisteForm
    template_name='sveuciliste_update.html'
    success_url=reverse_lazy('main:sveuciliste')

    def get_object(self, queryset=None):
        naziv_sveucilista=self.kwargs.get('naziv_sveucilista')
        return Sveuciliste.objects.get(naziv_sveucilista=naziv_sveucilista)

class LoginRegisterView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        register_form = UserCreationForm()
        return render(request, 'register.html', {
            'login_form': login_form,
            'register_form': register_form
        })

    def post(self, request):
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/pocetna')
            else:
                error_message = 'Invalid login'
        elif 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('/pocetna')
            else:
                error_message = 'Invalid registration'
        else:
            error_message = 'Invalid request'
        login_form = AuthenticationForm()
        register_form = UserCreationForm()
        return render(request, 'register.html', {
            'login_form': login_form,
            'register_form': register_form,
            'error_message': error_message
        })


## Create your views here.
@login_required
def main(request):
    return render(request, 'base_generic.html')
    # primjetiti korištenje HTML-a

@login_required
def mjesto_list(request):
    query=request.GET.get('search')
    if query:
        mjesta=Mjesto.objects.filter(
            Q(naziv_mjesta__icontains=query) |
            Q(postanski_broj__icontains=query) 
        )           
    else:
        mjesta=Mjesto.objects.all()
    return render(request, 'main/mjesto_list.html', {'object_list':mjesta})    


@login_required
def sveuciliste_list(request):
    query=request.GET.get('search')
    if query:
        sveucilista=Sveuciliste.objects.filter(
            Q(naziv_sveucilista__icontains=query) |
           
            Q(sveuciliste_postanski_broj__postanski_broj__icontains=query)
        )           
    else:
        sveucilista=Sveuciliste.objects.all()
    return render(request, 'main/sveuciliste_list.html', {'object_list':sveucilista})    


@login_required
def srednjaskola_list(request):
    query=request.GET.get('search')
    if query:
        srednje=SrednjaSkola.objects.filter(
            Q(naziv_srednje__icontains=query) |

            Q(srednja_postanski_broj__postanski_broj__icontains=query)
           
        )           
    else:
        srednje=SrednjaSkola.objects.all()
    return render(request, 'main/srednjaskola_list.html', {'object_list':srednje})    


@login_required
def fakultet_list(request):
    query=request.GET.get('search')
    if query:
        fakulteti=Fakultet.objects.filter(
            Q(fakultet__icontains=query) |
            Q(fakultet_sveuciliste__naziv_sveucilista__icontains=query)
        )           
    else:
        fakulteti=Fakultet.objects.all()
    return render(request, 'main/fakultet_list.html', {'object_list':fakulteti})    


@login_required
def smjer_list(request):
    query = request.GET.get('search')
    if query:
       smjers = Smjer.objects.filter(
            Q(naziv_smjera__icontains=query) |
            Q(fakultet__fakultet__icontains=query)
            
        )
    else:
        smjers = Smjer.objects.all()
    return render(request, 'main/smjer_list.html', {'object_list': smjers})
  

@login_required
def maturant_list(request):
    query = request.GET.get('search')
    if query:
        maturants = Maturant.objects.filter(
            Q(ime_maturanta__icontains=query) |
            Q(prezime_maturanta__icontains=query) |
            Q(upisni_broj__icontains=query) |
            Q(email_maturanta__icontains=query) |
            Q(maturant_postanski_broj__postanski_broj__icontains=query) |
            Q(maturant_smjer__naziv_smjera__icontains=query) |
            Q(maturant_srednja_skola__naziv_srednje__icontains=query) |
            Q(maturant_datum_upisa__icontains=query)
        )
    else:
        maturants = Maturant.objects.all()
    return render(request, 'main/maturant_list.html', {'object_list': maturants})


@login_required
def student_list(request):
    query = request.GET.get('search')
    if query:
        students = Student.objects.filter(
            Q(ime_studenta__icontains=query) |
            Q(prezime_studenta__icontains=query) |
            Q(jmbag_studenta__icontains=query) |
            Q(email_studenta__icontains=query) |
            Q(student_smjer__naziv_smjera__icontains=query) |
            Q(student_fakultet__fakultet__icontains=query) |
            Q(student_postanski_broj__postanski_broj__icontains=query) |
            Q(student_datum_upisa__icontains=query)
        )
    else:
        students = Student.objects.all()
    return render(request, 'main/student_list.html', {'object_list': students})



@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name='student_delete.html'
    success_url = reverse_lazy('main:student')

    def get_object(self, queryset=None):
        return self.model.objects.get(jmbag_studenta=self.kwargs['jmbag_studenta'])


@method_decorator(login_required, name='dispatch')
class MaturantDeleteView(DeleteView):
    model=Maturant
    template_name='maturant_delete.html'
    success_url=reverse_lazy('main:maturant')

    def get_object(self, queryset=None):
        return self.model.objects.get(upisni_broj=self.kwargs['upisni_broj'])    


@method_decorator(login_required, name='dispatch')
class MjestoDeleteView(DeleteView):
    model=Mjesto
    template_name='mjesto_delete.html'
    success_url=reverse_lazy('main:mjesto')

    def get_object(self, queryset=None):
        return self.model.objects.get(postanski_broj=self.kwargs['postanski_broj'])    
    


@method_decorator(login_required, name='dispatch')
class FakultetDeleteView(DeleteView):
    model=Fakultet
    template_name='fakultet_delete.html'
    success_url=reverse_lazy('main:fakultet')

    def get_object(self, queryset=None):
        return self.model.objects.get(fakultet=self.kwargs['fakultet'])    
    


@method_decorator(login_required, name='dispatch')
class SveucilisteDeleteView(DeleteView):
    model=Sveuciliste
    template_name='sveuciliste_delete.html'
    success_url=reverse_lazy('main:sveuciliste')

    def get_object(self, queryset=None):
        return self.model.objects.get(naziv_sveucilista=self.kwargs['naziv_sveucilista'])    
    

@method_decorator(login_required, name='dispatch')
class SmjerDeleteView(DeleteView):
    model=Smjer
    template_name='smjer_delete.html'
    success_url=reverse_lazy('main:smjer')

    def get_object(self, queryset=None):
        return self.model.objects.get(naziv_smjera=self.kwargs['naziv_smjera'])    
    

@method_decorator(login_required, name='dispatch')
class SrednjaDeleteView(DeleteView):
    model=SrednjaSkola
    template_name='srednjaskola_delete.html'
    success_url=reverse_lazy('main:srednja')

    def get_object(self, queryset=None):
        return self.model.objects.get(naziv_srednje=self.kwargs['naziv_srednje'])    
    
