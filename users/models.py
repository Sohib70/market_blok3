from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    tg_username = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/',default='avatars/default.jpg')

    def __str__(self):
        return str(self.username)

class Saved(models.Model):
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # body = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.author.username)