from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 120)
    age = models.IntegerField() 

    def __str__(self):
        return f"{self.username}'s Profile"
    

