from django.db import models

# Categorias dos estabelecimentos
class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

# Estabelecimentos
class Loja(models.Model):
    nome = models.CharField(max_length=200)
    categoria_loja = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.PROTECT, related_name='lojas')
    descricao = models.TextField(max_length=300)
    capa = models.ImageField(upload_to='aplicativo/imagens', verbose_name='Capa', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural =  'Lojas'
        ordering = ['nome']

# Categoria dos produtos
class Categoria_produto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria_produto'
        verbose_name_plural = 'Categoria_produtos'

# Produtos
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=300)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    adicionais = models.TextField(max_length=300, null=True, blank=True)
    loja = models.ForeignKey(Loja, verbose_name='Loja', on_delete=models.PROTECT, related_name='produtos')
    categoria = models.ForeignKey(Categoria_produto, verbose_name='Categoria do produto', on_delete=models.PROTECT, related_name='prod_categoria')

