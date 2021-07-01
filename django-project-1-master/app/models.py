from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.title
