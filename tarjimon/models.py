from django.db import models

# Create your models here.
class Lugat(models.Model):
    ingilizcha = models.CharField('Inglizcha',max_length=128)
    uzbekcha = models.CharField('uzbekcha',max_length=128)