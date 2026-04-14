from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    illness = models.CharField(max_length=100)
    prescription = models.TextField()
    bill_balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.illness}"
# Create your models here.
