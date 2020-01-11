from django.db import models

class KayitModel(models.Model):
    tcKimlikNo = models.BigIntegerField(default=0)
    adi = models.CharField(max_length=200)
    soyadi = models.CharField(max_length=200)
    cinsiyetCh = (("1","Erkek"),("2","Kız"))
    cinsiyet = models.CharField(max_length=20,choices=cinsiyetCh)
    telefon = models.CharField(blank=True,null=True,max_length=200)
    eposta = models.EmailField(default="aa@a.com",unique=True)


    def __str__(self):
        return self.adi + " " + self.soyadi + " " +str(self.tcKimlikNo)

    
