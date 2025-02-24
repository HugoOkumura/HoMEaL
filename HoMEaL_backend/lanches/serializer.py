from rest_framework import serializers
from .models import Lanche, Ingrediente, Produto
# from produto import Produto 



class ProdutoSerializer(serializers.ModelSerializer):
    pass


class IngredienteSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), write_only=True)

    class Meta:
        model = Ingrediente
        fields = ['id','produto_id','quantidade']

class LancheSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lanche
        fields = ['nome','descricao','preco','ingrediente']

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingrediente')
        lanche = Lanche.objects.create(**validated_data)

        for i in ingredientes_data:
            Ingrediente.objects.create(lanche=lanche, **i)

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', None)
        instance.nome = validated_data('nome', instance.nome)
        instance.descricao = validated_data('descricao', instance.descricao)
        instance.save()

        if ingredientes_data is not None:
            instance.ingredientes.all().delete
            for ingrediente in ingredientes_data:
                Ingrediente.objects.create(lanche=instance, **ingrediente)
        
        return instance
