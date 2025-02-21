from rest_framework import serializers
from .models import Lanche, Ingrediente
# from produto import Produto 



class ProdutoSerializer(serializers.ModelSerializer):
    pass


class IngredienteSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), write_only=True)

    class Meta:
        model = Ingrediente
        fields = ['id','produto','produto_id','quantidade']

class LancheSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lanche
        fields = ['nome','descricao','preco','ingrediente']