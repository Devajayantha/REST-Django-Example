from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    paradigma = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name, self.paradigma
