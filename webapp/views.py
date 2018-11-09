from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employess
from .serializers import employesSerializer
from . models import ejemplo
from .serializers import ejemploSerializer

class employeeList(APIView):

    def get(self, request):
        employess1 = employess.objects.all()
        serializer = employesSerializer(employess1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ejemploListcc(APIView):

    def get(self, request):
        ejme = ejemplo.objects.all()
        serializer = ejemploSerializer(ejme, many=True)
        return Response(serializer.data)

    def post(self):
        pass