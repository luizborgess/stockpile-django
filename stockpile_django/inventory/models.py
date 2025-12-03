from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    qty = models.IntegerField(default=0)
    threshold = models.IntegerField(default=0)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
