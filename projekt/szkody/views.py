from django.shortcuts import render
from szkody.models import *
from szkody.serializers import *
from rest_framework import generics
from rest_framework import permissions


class SamochodList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer


class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer


class CustomUserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class KlientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class ZdarzenieList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Zdarzenie.objects.all()
    serializer_class = ZdarzenieSerializer


class ZdarzenieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Zdarzenie.objects.all()
    serializer_class = ZdarzenieSerializer


class UczestnicyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Uczestnicy.objects.all()
    serializer_class = UczestnicySerializer


class UczestnicyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Uczestnicy.objects.all()
    serializer_class = UczestnicySerializer
