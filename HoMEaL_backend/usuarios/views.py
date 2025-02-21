from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


from .models import Cliente, Gerente, Usuario
from .serializer import ClienteSerializer, GerenteSerializer, UsuarioSerializer
from .permissions import GerentePermissao

# Create your views here.
class CriarConta(APIView):

    def get_permissions(self):
        if self.kwargs.get('tipo_usuario') == 'gerente':
            return [GerentePermissao(), IsAuthenticated()]
        return [AllowAny()]


    def get(self, request, tipo_usuario):
        data = Usuario.objects.all()
        serializer = UsuarioSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, tipo_usuario):
        if tipo_usuario == 'gerente':

            if not request.user.is_authenticated:
                return Response(
                    {
                        "detail": "Autenticação necessária para criar um Gerente.",
                        "redirect_url/": "/insira/url/da/pagina/login/no/front" # ALTERAR QUANDO O FRONT ESTIVER PRONTO
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            serializer_class = GerenteSerializer
        else:
            serializer_class = ClienteSerializer

        self.check_permissions(request)
        
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            usuario_data = serializer.validated_data.pop('usuario')
            email = usuario_data.get('email')
            password = usuario_data.get('password')

            usuario = Usuario.objects.create_user(email=email, password=password, tipo_usuario= tipo_usuario)

            if tipo_usuario == 'gerente':
                gerente = Gerente.objects.create(usuario=usuario, **serializer.validated_data)
                return Response(GerenteSerializer(gerente).data, status=status.HTTP_201_CREATED)
            else:
                cliente = Cliente.objects.create(usuario=usuario, **serializer.validated_data)
                return Response(ClienteSerializer(cliente).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


'''
{
    "usuario": {
        "email": "teste@gmail.com",
        "password": "123"
    },
    "nome":"teste",
    "endereco":"rua testando",
    "cpf":"12345678901"
}

'''