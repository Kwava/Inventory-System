from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=200, null=True,default=True)
    quantity=models.PositiveIntegerField( null=True)

    class Meta:
        verbose_name_plural='Product'
    
    def __str__(self):
        return (f'{self.name}{self.quantity}')
    

    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    staff=models.ForeignKey(User,on_delete=models.CASCADE)
    order_quantity=models.PositiveBigIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural='order'
    
    def __str__(self):
        return (f'{self.product} {self.staff.username}')

