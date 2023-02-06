from rest_framework import serializers
from .models import  Details, Names


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('__all__')


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = ('__all__')

