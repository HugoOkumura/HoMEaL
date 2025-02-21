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

    def post(self, request):
        if not request.is_authenticated:
            return Response({
                "detail":"Autenticação necessária para criar Lanche",
                "redirect_url":"/insira/url/da/pagina/login/no/front" # ALTERAR QUANDO O FRONT ESTIVER PRONTO"
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        
