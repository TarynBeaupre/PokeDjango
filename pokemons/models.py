from django.db import models


# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255, null=True)
    generation = models.IntegerField(null=True)
    classification = models.CharField(max_length=255, null=True)
    attack = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"
