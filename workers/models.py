import uuid
from django.db import models
from django.contrib.auth.models import User

class FieldWorker(models.Model):
    HARVEST = 'Harvest'
    PRUNING = 'Prunning'
    SCOUTING = 'Scouting'
    OTHER = 'Other'
    FUNCTION_CHOICES = [
        (HARVEST, 'Harvest'),
        (PRUNING, 'Pruning'),
        (SCOUTING, 'Scouting'),
        (OTHER, 'Other'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    function = models.CharField(
        max_length=8,
        choices=FUNCTION_CHOICES,
        default=OTHER,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name