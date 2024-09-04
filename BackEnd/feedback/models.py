from django.db import models
from django.utils import timezone
from recruitment_prosses.models import Recruitment_prosses
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import CustomUser


class Feedback(models.Model):
    
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prosses_id = models.ForeignKey(Recruitment_prosses, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    rating =  models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Рейтинг від 1 до 5"
    )
    feedback_text = models.TextField(blank=True)
    
    class Meta:
        db_table = "feedback"