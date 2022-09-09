from django.db import models

GENDER_CHOICES = (
    ('NA', "Unspecified"),
    ('NB', 'Non-Binary'),
    ('M', 'Male'),
    ('F', 'Female'),
)

class Pets(models.Model):
    pet_ID = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=120, default="", null=0, blank=0)
    pet_owner_name = models.CharField(max_length=120, default="")
    pet_age = models.IntegerField(default=0)
    pet_type = models.CharField(max_length=120, default="")
    pet_gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='NA')

