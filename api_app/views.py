from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonicaoSerializer
from .serializers import ArmaSerializer
from .models import CartItem
from .models import objeto_tipo
from .models import Arma
from .models import Monicao



class MonicaoViews(APIView):
    def post(self, request):
        serializer = ArmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ArmaViews(APIView):
    def post(self, request):
        serializer = ArmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

details =objeto_tipo.objects.create(tipo = '44')
details.save()

"""
{"product_name":"name",
  "product_price":"41",
  "product_quantity":"1"}
"""
