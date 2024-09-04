from django.db import models
from authentication.models import CustomUser


class Vacancie(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    level = models.CharField(max_length=20)
    budget = models.IntegerField()
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f"{self.name} - {self.level}"