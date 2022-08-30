from rest_framework import generics
from .models import Animal
from .permissions import IsOwnerOrReadOnly
from .serializers import AnimalSerializer

class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
