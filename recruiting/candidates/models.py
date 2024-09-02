from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(unique=True, max_length=20)
    telegram = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    cv = models.FileField(upload_to='all_cvs/', blank=True, null=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='candidates')
    vacancy_id = models.ForeignKey(Vacancies, on_delete=models.CASCADE, related_name='candidates')
    status = models.CharField(max_length=20)
    source = models.CharField(max_length=20, null=True)
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.vacancy_id}'
