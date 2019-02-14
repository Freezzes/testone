from django.db import models

# Create your models here.
class number(models.Model):
    numtext = models.CharField(max_length=20)
    count = models.IntegerField(default=1)
