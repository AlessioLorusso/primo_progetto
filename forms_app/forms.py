
from django import forms
from .models import Contatto

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
    
    #nome = forms.CharField()
    #cognome = forms.CharField()
    #email = forms.CharField()
    #contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}))
