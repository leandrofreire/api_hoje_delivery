from django.conf.urls import url
from . import views

urlpatterns = [
    url('categoria/', views.CategoriaList.as_view(), name='categoria-list'),
    url('lojas/', views.LojaList.as_view(), name='lojas-list'),
    url('categoria-produto/', views.CategoriaProdutoList.as_view(), name='categoria-produto-list'),
    url('produtos/', views.ProdutoList.as_view(), name='produtos-list')
]