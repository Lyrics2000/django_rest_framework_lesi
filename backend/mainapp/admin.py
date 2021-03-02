from django.contrib import admin

# Register your models here.
from .models import PersonalDetailsModel,VehicleDetailsModel

admin.site.register(PersonalDetailsModel)
admin.site.register(VehicleDetailsModel)