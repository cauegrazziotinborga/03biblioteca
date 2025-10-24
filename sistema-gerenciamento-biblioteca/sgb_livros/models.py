from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    ano_publicacao = models.PositiveIntegerField()
    editora = models.CharField(max_length=100, blank=True, null=True)
