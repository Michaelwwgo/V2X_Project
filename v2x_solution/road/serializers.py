from rest_framework import serializers
from v2x_solution.users import serializers as user_serializers
from . import models
 
class RoadSerializer(serializers.ModelSerializer):
 
     class Meta:
         model = models.Road
         fields = (
             'name',
             'location',
             'speed',
         )
 
class SituationSerializer(serializers.ModelSerializer):
 
    road = RoadSerializer()
    creator = user_serializers.UserSerializer()
    
    class Meta:
         model = models.Situation
         fields = (
             'id',
             'road',
             'isimpassable',
             'message',
             'startTime',
             'endTime',
             'creator'
         )
 
class InputSituationSerializer(serializers.ModelSerializer):
 
     class Meta:
         model = models.Situation
         fields = (
             'isimpassable',
             'message',
             'startTime',
             'endTime',
         )
