from rest_framework import serializers
from Kayit.models import KayitModel

class KayitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("tcKimlikNo","adi","soyadi","cinsiyet","telefon","eposta")
        model = KayitModel