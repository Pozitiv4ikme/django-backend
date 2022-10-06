from rest_framework import serializers
from helicopters.models import Helicopter


class HelicopterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Helicopter
        fields = ('id', 'name', 'amount_of_passengers', 'maximum_speed', 'price')


class HelicopterSerializersPUT(serializers.ModelSerializer):
    class Meta:
        model = Helicopter
        fields = ('name', 'amount_of_passengers', 'maximum_speed', 'price')
