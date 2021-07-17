from django.db import models

# Create your models here.
class Registration(models.Model):
	Firstname = models.CharField(max_length = 20)
	Lastname = models.CharField(max_length = 30)
	Email = models.EmailField(max_length = 50)
	Age = models.IntegerField()
	Photo = models.ImageField(upload_to='media/') 
	Password = models.CharField(max_length = 20)

class Registratione(models.Model):
	Picturename = models.CharField(max_length = 20)
	Description = models.CharField(max_length = 30)
	Price = models.IntegerField()
	Photo = models.ImageField(upload_to='media/') 



