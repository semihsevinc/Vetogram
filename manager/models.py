from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission, User
from typing import Set

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


    def multipleOwner(self):
        return self.patient_set.count() > 1

    def get_absolute_url(self):
        return '/owner/list'

    def __str__(self):
        return self.first_name + " " + self.last_name

class Patient(models.Model):
    DOG = 'DOG'
    CAT = 'CAT'
    BIRD = 'BIRD'
    FISH = 'FISH'
    OTHER = 'OTHER'
    ANIMAL_TYPE_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (BIRD, 'Bird'),
        (FISH, 'Fish'),
        (OTHER, 'Other'),
    ]
    animal_type = models.CharField(max_length=20, choices=ANIMAL_TYPE_CHOICES, default=OTHER)
    breed = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return '/patient/list'

    def __str__(self):
        return self.pet_name + ", " + self.animal_type