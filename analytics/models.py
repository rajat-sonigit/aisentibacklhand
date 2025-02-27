from django.db import models



from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    attrition_risk = models.CharField(max_length=10, default="Unknown")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]} - {self.sentiment}"
