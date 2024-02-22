from django import forms
from .models import Model1, Model2, Model3

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = '__all__'

class Model2Form(forms.ModelForm):
    class Meta:
        model = Model2
        fields = '__all__'

class Model3Form(forms.ModelForm):
    class Meta:
        model = Model3
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
