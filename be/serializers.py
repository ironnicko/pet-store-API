from email.policy import default
from  rest_framework import serializers
from .models import Pets

GENDER_CHOICES = (
    ('NA', "Unspecified"),
    ('NB', 'Non-Binary'),
    ('M', 'Male'),
    ('F', 'Female'),
)
class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ['pet_ID', 'pet_name', 'pet_owner_name', 'pet_age', 'pet_type', 'pet_gender']