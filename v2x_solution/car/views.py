from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Cars(APIView):

    def get(self, req, format=None):

        # 1. get all cars
        
        cars = models.Car.objects.all()

        serializer = serializers.CarSerializer(cars, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req, format=None):

        serializer = serializers.CarSerializer(data=req.data)

        if serializer.is_valid():
            
            serializer.save()
            
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CriminalCars(APIView):

    def get(self, req, format=None):
        
        # 1. get all criminalcars
        
        criminalcars = models.CriminalCar.objects.all()

        serializer = serializers.CriminalCarSerializer(criminalcars, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req, format=None):

        serializer = serializers.InputCriminalCarSerializer(data=req.data, partial=True)

        if serializer.is_valid():

            car_image = str(req.data.get('image'))
            car_image = car_image.split('.')
            car_number, car_location = car_image[0].split('_')
            
            found_car = models.Car.objects.get(number=car_number)

            serializer.save(car=found_car, creator=req.user, location=car_location)

            found_car.isFind = True

            found_car.save()

            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, req, format=None):

        print(req.data)

        serializer = serializers.InputCriminalCarSerializer(data=req.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostCars(APIView):

    def get(self, req, format=None):
        
        postcars = models.PostCar.objects.all()

        serializer = serializers.PostCarSerializer(postcars, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ModeratePostCars(APIView):
    
    def get(self, req, postcars_id, format=None):

        try:
            find_postcar = models.PostCar.objects.get(id=postcars_id)
        except models.PostCar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.MinimumPostCarSerializer(find_postcar)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, req, postcars_id, format=None):

        try:
            find_postcar = models.PostCar.objects.get(id=postcars_id)
        except models.PostCar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.PostCarSerializer(find_postcar, data=req.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(status=status.HTTP_200_OK)
        
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)