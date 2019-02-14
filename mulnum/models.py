from django.db import models

# Create your models here.
class number(models.Model):
    numtext = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.numtext