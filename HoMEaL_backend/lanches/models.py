from django.db import models

# from produtos.models import Produto

# Create your models here.

class Produto():
    pass


class Lanche(models.Model):
    nome = models.CharField(max_length= 20, unique=True)
    descricao = models.CharField(max_length=150, blank=True)
    preco = models.FloatField()



class Ingrediente(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="ingredientes")
    lanche = models.ForeignKey(Lanche, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('lanche','produto')