from django.db import models

class UserLogin(models.Model):
    firstname=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    mobile=models.BigIntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
