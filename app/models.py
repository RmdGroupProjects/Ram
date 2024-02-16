from django.db import models
class Register(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=36)
    gender=models.CharField(max_length=36)
    age=models.DateTimeField()
    phone=models.CharField(max_length=36)
    username=models.CharField(max_length=36)
    password=models.CharField(max_length=36)
    house =models.CharField(max_length=36)
    Village =models.CharField(max_length=36)
    Mandal =models.CharField(max_length=36)
    Distaic =models.CharField(max_length=36)
    States =models.CharField(max_length=36)
    PinCode =models.CharField(max_length=36)

class Photes(models.Model):
    idno=models.IntegerField(primary_key=True)
    images=models.ImageField(upload_to="media/")
class Total(models.Model):
    idno=models.IntegerField(primary_key=True)
    Total=models.CharField(max_length=30)
