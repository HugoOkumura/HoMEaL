from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from usuarios.models import Gerente, Usuario
from usuarios.permissions import GerentePermissao
from .models import Ingrediente, Lanche
from .serializer import IngredienteSerializer, LancheSerializer

# Create your views here.

class CriarLanche(APIView):
    permission_classes = [IsAuthenticated, GerentePermissao]

    def post(self, request):
        serializer = LancheSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
