from django.db import models
from django.urls import reverse


class Categoria (models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("main:listar_produtos_por_categoria", args=[self.slug])


class Produto (models.Model):
    categoria = models.ForeignKey(
        "Categoria", related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='imagens-produtos', blank=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("main:detalhes_produto", args=[self.id, self.slug])


class Loja(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    UF = models.CharField(max_length=2)
    CEP = models.CharField(max_length=8)
    email = models.EmailField()
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    UF = models.CharField(max_length=2)
    CEP = models.CharField(max_length=8)

    def __str__(self):
        return self.logradouro


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.nome

# Create your models here.
