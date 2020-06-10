from rest_framework import serializers
from .models import Categoria, Loja, Categoria_produto, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'

class CategoriaProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_produto
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'