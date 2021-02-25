from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    name=models.CharField(max_length=200,default="",blank=True)
    title = models.CharField(max_length=200)
    body=models.TextField()     
    date=models.DateTimeField(auto_now_add=True)
    pic=models.ImageField(default='default.png',blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def snippet(self):
        return self.body[0:50]+"......"


#python manage.py makemigrations
#python manage.py migrate

def __str__(self):
    return self.title
