
# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_joined = models.DateField(null=True, blank=True) 
    sentiment_score = models.FloatField(default=0.0)  # Store average sentiment score
    attrition_risk = models.CharField(
        max_length=10, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], default="Low"
    )
    date_joined = models.DateField()

    def __str__(self):
        return self.name
