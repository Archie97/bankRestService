from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Bank

from .serializers import BankSerializer
from rest_framework import generics

class ListBankView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class DetailBankView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CreateBankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer