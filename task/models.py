from django.db import models
from django.utils.text import slugify

class Task(models.Model):
    tarefa = models.CharField(max_length=200, unique=True, error_messages={"unique":"Tarefa já existente."})
    descricao = models.TextField(null=True, blank=True)
    feito = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tarefa, allow_unicode=True)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.tarefa

