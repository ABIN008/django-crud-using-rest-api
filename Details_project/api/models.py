from django.db import models

# Create your models here.

class Names(models.Model):
    sports=models.CharField(max_length=100,unique=True)

def __str__(self):
    return self.department


class Details(models.Model):
    Student_name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    date_of_birth=models.DateField(auto_now_add=True)
    sports_item=models.ForeignKey(Names,on_delete=models.CASCADE)


def __str__(self):
    return self.department
