from django.db import models


# Create your models here.
# Класс создания таблицы логина и пароля в БД.
class RegistrationPerson(models.Model):
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    age = models.IntegerField(blank=True, null=True)
    objects = models.Manager()
    DoesNotExist = models.Manager()
