from django.db import models

# Create your models here.
from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True, null=True)  # Store sentiment analysis
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.created_at}"
