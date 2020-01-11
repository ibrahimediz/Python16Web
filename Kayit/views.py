from django.shortcuts import render
from .models import KayitModel

def kayitListele(request):
    kayitlar = KayitModel.objects.all()
    return render(request,"index.html",{"kayitlar":kayitlar})