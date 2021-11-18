from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback = models.TextField(max_length=500, null=False, blank=False)
    def __str__(self):
        return self.feedback
