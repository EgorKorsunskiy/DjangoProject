from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=10, null=True)
    text = models.TextField()
    publication_data = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.SET_DEFAULT, default='Deleted')
    ad = models.Manager()


class User(models.Model):
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=36, default='1111')
    email = models.EmailField(null=True)
    age = models.IntegerField()
    rating = models.IntegerField(default=0)
    vip_status = models.BooleanField(default=False)
    photo = models.ImageField(null=True, upload_to='./ad/templates/ad/')
    user = models.Manager()
