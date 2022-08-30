from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'species', 'description')
        model = Animal