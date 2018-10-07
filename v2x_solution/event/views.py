from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from v2x_solution.road import models as road_models

class Events(APIView):

    def get(self, req, format=None):

        # 1. get all events

        events = models.Event.objects.all()

        serializer = serializers.EventSerializer(events, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, req, format=None):

        user = req.user

        # 1. check query

        try:
            found_road = road_models.Road.objects.get(name=req.data.get('location'))
        except road_models.Road.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.EventSerializer(data=req.data)

        if serializer.is_valid():
            
            # 2. save event

            serializer.save(creator=user, road=found_road)
            
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class ModerateEvent(APIView):
    
    # find event
    def find_event(self, event_id):

        try:
            found_event = models.Event.objects.get(id=event_id)
            return found_event
        except models.Event.DoesNotExist:
            return None

    # select event
    def get(self, req, event_id, format=None):

        # 1. find event

        event = self.find_event(event_id)

        if event is None:

            return Response(status=status.HTTP_404_NOT_FOUND)
        
        else:
            
            # 2. serialize data
             
            serializer = serializers.EventSerializer(event)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

    # update event
    def put(self, req, event_id, format=None):
        
        # 1. find event
        
        event = self.find_event(event_id)

        if event is None:

            return Response(status=status.HTTP_404_NOT_FOUND)

        # 2. check event's creator

        elif event.creator != req.user:

            return Response(status.HTTP_401_UNAUTHORIZED)

        # 3. check serializer's data

        else:
        
            serializer = serializers.EventSerializer(event, data=req.data, partial=True)

        if serializer.is_valid():

            serializer.save(creator=req.user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # delete event
    def delete(self, req, event_id, format=None):

        # 1. find event
        
        event = self.find_event(event_id)

        if event is None:

            return Response(status=status.HTTP_404_NOT_FOUND)

        # 2. check event's creator

        elif event.creator != req.user:

            return Response(status.HTTP_401_UNAUTHORIZED)

        # 3. delete serializer's data

        else:
        
            event.delete()

            return Response(status=status.HTTP_200_OK)

class Search(APIView):
    
    def get(self, req, format=None):

        event_name = req.query_params.get('name', None)
        event_time = req.query_params.get('time', None)
        event_location = req.query_params.get('location', None)

        # 1. if url is /events/search/?name= 
        # ex: /events/search/?name=행사

        if event_name is not None:

            events = models.Event.objects.filter(name__istartswith=event_name)

            serializer = serializers.EventSerializer(events, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        # 2. url is /events/search/?time=
        # ex: /events/search/?time=2018-07-12

        if event_time is not None:

            events = models.Event.objects.filter(time__istartswith=event_time)

            serializer = serializers.EventSerializer(events, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        # 3. url is /events/search/?location=
        # ex: /events/search/?location=inha-ro

        if event_location is not None:

            events = models.Event.objects.filter(road__name__istartswith=event_location)

            serializer = serializers.EventSerializer(events, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        # 4. all param is None

        return Response(status=status.HTTP_404_NOT_FOUND)

