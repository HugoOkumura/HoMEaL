from rest_framework import serializers
from .models import Usuario, Cliente, Gerente


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email','tipo_usuario']

    # def create(self, validated_data):
    #     usuario_data = validated_data.pop('usuario')
    #     usuario = Usuario.objects.create_user(**usuario_data, )

class ClienteSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer()
    # email = serializers.CharField(source="usuario.email", read_only=True)
    # tipo_usuario = serializers.CharField(source="usuario.tipo_usuario", read_only=True)
    class Meta:
        model = Cliente
        fields = ['usuario', 'nome', 'endereco', 'cpf']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data, tipo_usuario='cliente')
        cliente = Cliente.objects.create(usuario=usuario, **validated_data)
        return cliente
        

class GerenteSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(source="usuario.email", read_only=True)
    # tipo_usuario = serializers.CharField(source="usuario.tipo_usuario", read_only=True)
    usuario = UsuarioSerializer()
    class Meta:
        model = Gerente
        fields = ['usuario','nome','endereco','cpf','data_inicio','ainda_trabalha','data_final']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data, tipo_usuario='gerente')
        gerente = Gerente.objects.create(usuario=usuario, **validated_data)
        return gerente


