from django.db import models

class Departament(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=48)
    departament = models.ForeignKey(
        Departament,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name
