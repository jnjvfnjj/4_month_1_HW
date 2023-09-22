from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="фамилия"
    )
    age = models.IntegerField(
        verbose_name="возраст"
        
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="телефонный номер"
    )
    email = models.EmailField(
        verbose_name="email"
    )

