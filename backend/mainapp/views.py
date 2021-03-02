from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import PersonalDetailsModel,VehicleDetailsModel
from .serializer import personalDetailsModelSerializer,VehicleDetailsModelSerializers

# Create your views here.
from braces.views import CsrfExemptMixin
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class PersonaldetailsPost(CsrfExemptMixin,APIView):
    authentication_classes = []
    def post(self, request, format=None):
        serializer = personalDetailsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicledetailsPost(CsrfExemptMixin,APIView):
    authentication_classes = []
    def post(self, request, format=None):
        serializer = VehicleDetailsModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



