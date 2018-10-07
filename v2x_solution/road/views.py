from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Roads(APIView):

    def get(self, req, format=None):

        # 1. get all roads
        
        roads = models.Road.objects.all()

        serializer = serializers.RoadSerializer(roads, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class Situations(APIView):

    def get(self, req, format=None):
        
        # 1. get all situations
        
        situations = models.Situation.objects.all()

        serializer = serializers.SituationSerializer(situations, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req, format=None):

        # 1. find road
        try:
            found_road = models.Road.objects.get(name=req.data.get('name'))
        except models.Road.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 2. check query

        serializer = serializers.InputSituationSerializer(data=req.data)

        if serializer.is_valid():
            
            # 3. save situation

            serializer.save(road=found_road, creator=req.user)
            
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class ModerateSituation(APIView):
    
    # find situation
    def find_situation(self, situation_id):

        try:
            found_situation = models.Situation.objects.get(id=situation_id)
            return found_situation
        except models.Situation.DoesNotExist:
            return None

    # select situation
    def get(self, req, situation_id, format=None):

        # 1. find situation

        situation = self.find_situation(situation_id)

        if situation is None:

            return Response(status=status.HTTP_404_NOT_FOUND)
        
        else:
            
            # 2. serialize data
             
            serializer = serializers.SituationSerializer(situation)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

    # update situation
    def put(self, req, situation_id, format=None):
        
        # 1. find situation
        
        situation = self.find_situation(situation_id)

        if situation is None:

            return Response(status=status.HTTP_404_NOT_FOUND)

        # 2. check situation's creator

        elif situation.creator != req.user:

            return Response(status.HTTP_401_UNAUTHORIZED)

        # 3. check serializer's data

        else:
        
            serializer = serializers.SituationSerializer(situation, data=req.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete situation
    def delete(self, req, situation_id, format=None):

        # 1. find situation
        
        situation = self.find_situation(situation_id)

        if situation is None:

            return Response(status=status.HTTP_404_NOT_FOUND)

        # 2. check situation's creator

        elif situation.creator != req.user:

            return Response(status.HTTP_401_UNAUTHORIZED)

        # 3. delete serializer's data

        else:
        
            situation.delete()

            return Response(status=status.HTTP_200_OK)

class Search(APIView):
    
    def get(self, req, format=None):

        situation_road_name = req.query_params.get('name', None)
        situation_isimpassable = req.query_params.get('isimpassable', None)

        # 1. if url is /roads/situation/search/?name= 
        # ex: /roads/situation/search/?name=inha-ro

        if situation_road_name is not None:

            situations = models.Situation.objects.filter(road__name__istartswith=situation_road_name)

            serializer = serializers.SituationSerializer(situations, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        # 2. url is /roads/situation/search/?isimpassable=
        # ex: /roads/situation/search/?isimpassable=True

        if situation_isimpassable is not None:

            situations = models.Situation.objects.filter(isimpassable=situation_isimpassable)

            serializer = serializers.SituationSerializer(situations, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        # 3. all param is None

        return Response(status=status.HTTP_404_NOT_FOUND)
