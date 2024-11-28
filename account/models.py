
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE)
    adress=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=20, null=True)
    image=models.ImageField(upload_to='images_profile',blank=True,null=True)

    def __str__(self):
        return f'{self.staff.username}'
    

