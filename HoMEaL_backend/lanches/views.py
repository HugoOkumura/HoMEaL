from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from usuarios.models import Gerente, Usuario
from usuarios.permissions import GerentePermissao
from .models import Ingrediente, Lanche
from .serializer import IngredienteSerializer, LancheSerializer

# Create your views here.

class LancheManager(APIView):
    permission_classes = [IsAuthenticated(), GerentePermissao()]

    def post(self, request):
        serializer = LancheSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, lanche_id):
        try:
            lanche = Lanche.objects.get(id=lanche_id)
        except Lanche.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LancheSerializer(lanche, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)    

        

class ListarLanches(APIView):
    permission_classes = [AllowAny()]

    def get(self, request):
        data = Lanche.objects.all()

        serializer = LancheSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

