from django.db import models

class Student1(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=70)
