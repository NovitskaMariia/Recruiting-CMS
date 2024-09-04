from django.db import models
from employees.models import Employees


class Vacancies(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    level = models.CharField(max_length=20)
    budget = models.IntegerField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f"{self.name} - {self.level}"