from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering=['name']
      

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField( max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering=['name']
    