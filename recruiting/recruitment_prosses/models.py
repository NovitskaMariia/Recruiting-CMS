from django.db import models
from django.utils import timezone


class Stages(models.Model):
    
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "industries"


class Recruitment_prosses(models.Model):
    
    id = models.AutoField(primary_key=True)
    # candidate_id = models.ForeignKey()
    stage = models.ForeignKey(Stages, related_name="satge", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
    
    class Meta:
        db_table = "recruitment_prosses"