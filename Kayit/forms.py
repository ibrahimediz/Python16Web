from django import forms
from .models import KayitModel

class KayitForm(forms.ModelForm):

    class Meta:
        model = KayitModel
        fields = ("tcKimlikNo","adi","soyadi","cinsiyet","telefon","eposta")