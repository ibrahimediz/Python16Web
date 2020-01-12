from django import forms
from .models import KayitModel

class KayitForm(forms.ModelForm):

    class Meta:
        model = KayitModel
        labels={
            "tcKimlikNo":"T.C. Kimlik No",
            "adi":"Adı",
            "soyadi":"Soyadı",
            "cinsiyet":"Cinsiyet",
            "telefon":"Telefon",
            "eposta":"E Posta Adresi"
        }
        fields = ("tcKimlikNo","adi","soyadi","cinsiyet","telefon","eposta")