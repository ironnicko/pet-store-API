from be.models import Pets
from be.serializers import PetsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PetsList(APIView):

    def get(self, request, format=None):
        pets = Pets.objects.all()
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, format=None):
        Pets.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


class PetsDetail(APIView):

    def error_checker(self, pk):
        try:
            pet = Pets.objects.get(pet_ID=pk)
            return pet
        except Pets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        pet = self.error_checker(pk)
        serializer = PetsSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pet = self.error_checker(pk)
        serializer = PetsSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pet = self.error_checker(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)