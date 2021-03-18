from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length = 100, blank = False)
    EmailAddress = models.CharField(max_length = 100, blank = False)
    Password = models.TextField(max_length = 65000, blank = False)

    def __str__(self):
        return self.EmailAddress
