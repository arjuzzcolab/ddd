from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_media')

class Register(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    con_password = models.CharField(max_length=200)

class Login(models.Model):
  
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

