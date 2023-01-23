from rest_framework import viewsets, generics

from .models import *
from .shemas import *

class CameraSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializers

class Laurent2Set(viewsets.ModelViewSet):
    queryset = Laurent2.objects.all()
    serializer_class = Laurent2Serializers

class LEDBoardSet(generics.ListCreateAPIView):
    queryset = LEDBoard.objects.all()
    serializer_class = LEDBoardSerializers

class BlackListItemSet(viewsets.ModelViewSet):
    queryset = BlackListItem.objects.all()
    serializer_class = BlackListItemSerializers

class BlackListItemCheck(generics.RetrieveAPIView):
    queryset = BlackListItem.objects.all()
    serializer_class = BlackListItemSerializers

class CarParkItemSet(viewsets.ModelViewSet):
    queryset = CarParkItem.objects.all()
    serializer_class = CarParkItemSerializers

