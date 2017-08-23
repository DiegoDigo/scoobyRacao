from rest_framework.serializers import ModelSerializer
from produto.models import Produto, Categoria, Animal


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class AnimaloSerializer(ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    animal = CategoriaSerializer(read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'



