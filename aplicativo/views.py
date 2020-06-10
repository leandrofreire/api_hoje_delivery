from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Loja, Categoria_produto, Produto
from .serializers import CategoriaSerializer, LojaSerializer, CategoriaProdutosSerializer, ProdutoSerializer

# Create your views here.
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LojaList(generics.ListCreateAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class CategoriaProdutoList(generics.ListCreateAPIView):
    queryset = Categoria_produto.objects.all()
    serializer_class = CategoriaProdutosSerializer

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer