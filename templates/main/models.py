from django.db import models

# Create your models here.


class Films(models.Model):
    title = models.CharField(max_length=250)
    producer = models.CharField(max_length=250)
    rating = models.FloatField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title