from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^produto/$', views.Produtos.as_view()),
    url(r'^produto/(?P<id>\d+)/$', views.ProdutoCategoria.as_view()),
    url(r'^produto/(?P<categoriaId>\d+)/animal/(?P<animalId>\d+)/$', views.ProdutoCategoriaAnimal.as_view()),
    url(r'^produto/animal/(?P<id>\d+)/$', views.ProdutoAnimal.as_view()),
    url(r'^usuario/', include('usuario.api.urls')),
]
