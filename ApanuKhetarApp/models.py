from django.db import models

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    Status = models.CharField(max_length=10,default="Deactive")

    def __str__(self):
        return self.Email + " | " + self.FirstName