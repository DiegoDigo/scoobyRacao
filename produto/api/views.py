from rest_framework import generics
from produto.models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer


class Produtos(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoCategoria(generics.ListAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        return Produto.objects.produtoCategoria(self.kwargs['id'])


class ProdutoAnimal(generics.ListAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        return Produto.objects.produtoAnimal(self.kwargs['id'])


class ProdutoCategoriaAnimal(generics.ListAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        return Produto.objects.produtoCategoriaAnimal(self.kwargs['categoriaId'], self.kwargs['animalId'])
