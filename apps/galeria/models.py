from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):

    Opcoes_Categoria = [
        ('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=250, null=False, blank=False)
    legenda = models.CharField(max_length=250, null=False, blank=False)
    categoria = models.CharField(max_length=250,  choices= Opcoes_Categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    mais_vistas = models.IntegerField(default=0)
    mais_curtidas = models.IntegerField(default=0)
    surpreenda_me = models.URLField(default='https://picsum.photos/200/300', null=True, blank=True)
    favoritas = models.BooleanField(default=False)

    def __str__(self):
        return self.nome