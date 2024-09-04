from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)
    role = models.IntegerField()
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

