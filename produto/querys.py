from django.db import models


class QuerySetProduto(models.query.QuerySet):

    def produtoCategoria(self, categoriaId):
        return self.filter(categoria=categoriaId)

    def produtoAnimal(self, animalId):
        return self.filter(animal=animalId)

    def produtoCategoriaAnimal(self, categoriaId, animalId):
        return self.filter(animal=animalId, categoria=categoriaId)