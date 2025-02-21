from rest_framework import serializers
from .models import Usuario, Cliente, Gerente

'''
    Devido ao jeito que foi feito a modelagem dos usuários, para poder mostrar todas as informações necessários do usuário
    foi preciso implementar os serializers desta forma.

    Exemplo de como ficaria o JSON:
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



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email','tipo_usuario']



class ClienteSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer()

    class Meta:
        model = Cliente
        fields = ['usuario', 'nome', 'endereco', 'cpf']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data, tipo_usuario='cliente')
        cliente = Cliente.objects.create(usuario=usuario, **validated_data)
        return cliente
        

class GerenteSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer()
    class Meta:
        model = Gerente
        fields = ['usuario','nome','endereco','cpf','data_inicio','ainda_trabalha','data_final']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data, tipo_usuario='gerente')
        gerente = Gerente.objects.create(usuario=usuario, **validated_data)
        return gerente


