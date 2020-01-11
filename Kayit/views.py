from django.shortcuts import render,get_object_or_404
from .models import KayitModel


def kayitListele(request):
    kayitlar = KayitModel.objects.all()
    return render(request,"Kayit/liste.html",{"kayitlar":kayitlar})

def kayitdetay(request,tcKimlikNo):
    kayit = KayitModel.objects.get(tcKimlikNo=tcKimlikNo)
    return render(request,"Kayit/detay.html",{"kayit":kayit})
