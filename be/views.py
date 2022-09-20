from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pyrebase
from os import getenv
from dotenv import load_dotenv

load_dotenv()

config = {
  "apiKey":getenv('apikey'),
  "authDomain":getenv('authDomain'),
  "projectId":getenv('projectId'),
  "storageBucket":getenv('storageBucket'),
  "messagingSenderId":getenv('messagingSenderId'),
  "databaseURL" : getenv('databaseURL'),
  "appId":getenv('appId')
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
db=firebase.database()

class PetsList(APIView):

    def sanity_check(self):
        if db.child("Pets").get().val() == None:
            db.child("Pets").set({" " : ""})

    def get(self, request, format=None):
        self.sanity_check()
        pets = db.child("Pets").get()
        return Response(pets.val())

    def post(self, request, format=None):
        self.sanity_check()
        try:
            flag = str(request.data["pet_ID"]) in db.child("Pets").get().val()
            if flag:
                raise EOFError
            db.child("Pets").child(request.data["pet_ID"]).set(request.data)
            return Response("CREATED!", status=status.HTTP_201_CREATED)
        except:
            return Response("Error Occurred! Try changing the ID of the PET", status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, format=None):
        db.child("Pets").remove()
        self.sanity_check()
        return Response("Deleted ALL!", status=status.HTTP_200_OK)


class PetsDetail(APIView):


    def sanity_check(self):
        if db.child("Pets").get().val() == None:
            db.child("Pets").set({" " : ""})

    def get(self, request, pk, format=None):
        self.sanity_check()
        pet = db.child("Pets").child(pk).get().val()
        return Response(pet)

    def put(self, request, pk, format=None):
        self.sanity_check()
        try:
            pet = request.data
            db.child("Pets").child(pk).update(pet)
            return Response("Updated", status=status.HTTP_200_OK)
        except:
            return Response("Error!", status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, pk):
        db.child("Pets").child(pk).remove()
        self.sanity_check()
        return Response("Deleted Pet!", status=status.HTTP_204_NO_CONTENT)