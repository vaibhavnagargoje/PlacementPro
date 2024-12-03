from django.db import models

# Create your models here.

class Batch(models.Model):
    name = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    

    def __str__(self):
        return f" {self.name} - {self.start_year}-{self.end_year}"