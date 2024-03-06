from django.db import models

from datetime import datetime

class Fotografia(models.Model):

    Opcoes_Categoria = [
        ('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=250, null=False, blank=False)
    legenda = models.CharField(max_length=250, null=False, blank=False)
    categoria = models.CharField(max_length=250,  choices= Opcoes_Categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'