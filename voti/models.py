from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materie"
    
class Voti(models.Model):
    nomeP = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    voto = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeP+ " " + self.materia+ " " + self.voto
    
    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Voti"