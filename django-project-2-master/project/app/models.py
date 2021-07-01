from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.title
