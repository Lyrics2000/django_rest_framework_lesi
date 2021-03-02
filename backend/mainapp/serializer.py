from rest_framework import serializers

from .models import PersonalDetailsModel,VehicleDetailsModel


class personalDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetailsModel
        fields = ["name_of_customer","tag_no","id_no","email"]

class VehicleDetailsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetailsModel
        fields = ["customer","vehicle_registration_no","log_book","vehicle_make"]

        
