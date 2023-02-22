from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class MaturantForm(ModelForm):
    class Meta:
        model=Maturant
        fields = '__all__'        

class FakultetForm(ModelForm):
    class Meta:
        model=Fakultet
        fields='__all__'        

class SmjerForm(ModelForm):
    class Meta:
        model=Smjer
        fields='__all__'        
        
class SrednjaForm(ModelForm):
    class Meta:
        model=SrednjaSkola
        fields='__all__'        

class MjestoForm(ModelForm):
    class Meta:
        model=Mjesto
        fields='__all__'     

class SveucilisteForm(ModelForm):
    class Meta:
        model=Sveuciliste
        fields='__all__'           