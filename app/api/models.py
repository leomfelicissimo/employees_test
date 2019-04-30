from django.db import models

class Department(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False,
    )
    description = models.CharField(
        max_length=64,
        blank=False,
    )

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
    )
    email = models.CharField(
        max_length=48,
        blank=False,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
    )
        
    def __str__(self):
        return self.name
