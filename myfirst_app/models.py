from django.db import models
from django.contrib.auth.models import User

class UserProf(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='media/first_app',blank=True)

    def __str__(self):
        return self.user.username
# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic=models.ForeignKey('Topic',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=256,unique=True)
    url=models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey('Webpage',on_delete=models.DO_NOTHING)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
