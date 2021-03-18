from django.db import models

# Create your models here.

class Product(models.Model):
    ProductName = models.CharField(max_length= 100, blank = True)
    ProductDescription = models.CharField(max_length= 100, blank = True)
    ProductQuantity = models.IntegerField(blank = True)

    def __str__(self):
        return self.ProductName
