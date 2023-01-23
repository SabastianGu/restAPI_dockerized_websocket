from rest_framework import serializers
from .models import *

class CameraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = "__all__"

class Laurent2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Laurent2
        fields = "__all__"

class LEDBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = LEDBoard
        fields = "__all__"

class BlackListItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlackListItem
        fields = "__all__"

class CarParkItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarParkItem
        fields = "__all__"

class WorkingModeSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkingMode
        fields = "__all__"

class AccessPointSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccessPoint
        fields = "__all__"
