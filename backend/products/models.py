from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    def get_discount(self):
        return "123"
