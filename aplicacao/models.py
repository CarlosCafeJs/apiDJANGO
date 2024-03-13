from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=9)
    valor = models.CharField(max_length=5)
    validade = models.DateField()

    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    NIVEL = (
        ('A', 'Maior Qualidade'),
        ('B', 'Boa Media'),
        ('C', 'Media Qualidade'),
        ('D', 'Pior Qualidade'),
        
    )
    nome_marca = models.CharField(max_length=15)
    slogan = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15, choices=NIVEL, blank=False, null=False, default='C')

    def __str__(self):
        return self.nome_marca

