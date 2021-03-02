
from django.contrib import admin
from django.urls import path
from .views import index,PersonaldetailsPost,VehicledetailsPost

app_name = 'mainapp'


urlpatterns = [
    path('',index, name = "index_page"),
    path('apiv01/personal_details/',PersonaldetailsPost.as_view(), name = "personal_details"),
    path('apiv01/vehicle_details/',VehicledetailsPost.as_view(), name = "vehicle_details")
    
   
]