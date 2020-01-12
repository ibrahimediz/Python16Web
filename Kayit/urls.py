from django.urls import path
from . import views

urlpatterns = [
    path('',views.kayitListele,name="kayitList"),
    path('<int:pk>',views.kayitdetay2,name="kayitdetay2"),
    path('tc/<int:tcKimlikNo>',views.kayitdetay,name="detayTC"),
    path('yeni',views.kayitYeni,name="kayityeni"),
    path('duzenle/<int:pk>',views.kayitDuzenle,name="kayitduzenle"),
]
