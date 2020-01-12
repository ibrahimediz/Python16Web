from django.shortcuts import render,get_object_or_404,redirect
from .models import KayitModel
from .forms import KayitForm


def kayitListele(request):
    kayitlar = KayitModel.objects.all()
    return render(request,"Kayit/liste.html",{"kayitlar":kayitlar})

def kayitdetay(request,tcKimlikNo):
    kayit = KayitModel.objects.get(tcKimlikNo=tcKimlikNo)
    return render(request,"Kayit/detay.html",{"kayit":kayit})

def kayitdetay2(request,pk):
    kayit = KayitModel.objects.get(pk=pk)
    return render(request,"Kayit/detay.html",{"kayit":kayit})

def kayitYeni(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            kayit = form.save(commit=False)
            kayit.save()
            return redirect('kayitdetay2',pk=kayit.pk)
    else:
        form = KayitForm()
    return render(request,'Kayit/kayitedit.html',{"form":form})