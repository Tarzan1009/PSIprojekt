from rest_framework import serializers
from szkody.models import *


class SamochodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samochod
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class ZdarzenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zdarzenie
        fields = '__all__'


class UczestnicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Uczestnicy
        fields = '__all__'
