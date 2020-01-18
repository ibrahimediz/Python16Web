
from Kayit.models import KayitModel
from .serializers import KayitSerializer

# from rest_framework import generics
# class ListTodo(generics.ListCreateAPIView):
#     queryset = KayitModel.objects.all()
#     serializer_class = KayitSerializer

# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = KayitModel.objects.all()
#     serializer_class = KayitSerializer

from rest_framework import viewsets

class KayitViewSet(viewsets.ModelViewSet):
    queryset = KayitModel.objects.all()
    serializer_class = KayitSerializer    