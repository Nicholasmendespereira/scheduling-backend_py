from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    create = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

class Agendamento(models.Model):
    hour = models.CharField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=30, null=True, blank=True)
    usuario_id = models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='Userario_id'
    )