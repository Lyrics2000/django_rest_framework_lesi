from django.db import models

# Create your models here.

class PersonalDetailsModel(models.Model):
    name_of_customer = models.CharField(max_length=255)
    tag_no = models.CharField(max_length=155)
    id_no =  models.IntegerField()
    email =  models.EmailField()

    def __str__(self):
        return self.name_of_customer

class VehicleDetailsModel(models.Model):
    customer = models.ForeignKey(PersonalDetailsModel,on_delete=models.CASCADE)
    vehicle_registration_no = models.CharField(max_length=255)
    log_book = models.CharField(max_length=255)
    vehicle_make = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_registration_no
    
    
