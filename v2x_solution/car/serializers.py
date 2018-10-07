from rest_framework import serializers
from v2x_solution.users import serializers as user_serializers
from . import models

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = (
            'number',
            'isFind',
            'message'
        )

class CriminalCarSerializer(serializers.ModelSerializer):

    car = CarSerializer()

    class Meta:
        model = models.CriminalCar
        fields = (
            'car',
            'image',
            'location',
            'creator',
            'created_at'
        )

class InputCriminalCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CriminalCar
        fields = (
            'image',
            'location',
            'creator'
        )

class PostCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostCar
        fields = (
            'id',
            'name',
            'number',
            'owner',
            'location',
        )

class MinimumPostCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostCar
        fields = (
            'location',
        )