from django.db import models


class Img(models.Model):
    Image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=30)


class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)


