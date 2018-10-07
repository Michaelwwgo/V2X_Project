from rest_framework import serializers
from . import models
 
class UserSerializer(serializers.ModelSerializer):

     class Meta:
         model = models.User
         fields = (
             'username',
             'phone',
             'coin',
         )
 
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User
        fields = (
            'username',
            'coin',   
        )