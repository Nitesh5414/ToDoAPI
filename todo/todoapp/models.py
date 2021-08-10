from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)
    object = models.Manager()

    def __str__(self):
        return self.title