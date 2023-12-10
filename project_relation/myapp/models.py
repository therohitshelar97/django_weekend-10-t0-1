from django.db import models

# Create your models here.

#This is one to one realtionship in django
class Person(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class AdharCard(models.Model):
    adhar_no = models.BigIntegerField(null=True,unique=True)
    person = models.OneToOneField(Person,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.adhar_no)
    
#one To many relations

class Person1(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Cars(models.Model):
    carName = models.CharField(max_length=100,null=True)
    person1 = models.ForeignKey(Person1,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.carName
    
#Many To Many In Django
class Students(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=100,null=True)
    students = models.ManyToManyField(Students,null=True) 

    def __str__(self):
        return self.book_name
