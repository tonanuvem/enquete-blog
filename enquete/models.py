from django.db import models
from django.utils import timezone

# Create your models here.

class Questao(models.Model):
    questao_pergunta = models.CharField(max_length=200)
    questao_data_pub = models.DateTimeField('Data de publicacao')
    def __str__(self):
        return self.questao_pergunta
    def idade_publicacao(self):
        delta = timezone.now() - self.questao_data_pub
        return delta.days
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Escolhas(models.Model):
    questao_fk = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=200)
    qtd_votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_escolha