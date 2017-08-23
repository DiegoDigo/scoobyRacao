from rest_framework import generics
from produto.models import Produto
from .serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated


class Produtos(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [IsAuthenticated]


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
