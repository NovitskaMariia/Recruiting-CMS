from django.db import models
from django.utils import timezone
from candidates.models import Candidate


class Stages(models.Model):
    
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "stages"


class Recruitment_prosses(models.Model):
    
    id = models.AutoField(primary_key=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stages, related_name="stage", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
    
    class Meta:
        db_table = "recruitment_prosses"