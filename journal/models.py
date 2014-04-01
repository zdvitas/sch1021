from django.db import models
from django.contrib.auth.models import User , UserManager


# Create your models here.

class CustomUser(User):
    cabinet = models.CharField(max_length=20)
    object = UserManager()


class Task(models.Model):
    tittle = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(CustomUser)
    status = models.BooleanField()
    cabinet = models.CharField(max_length=200)
    # status_class = models.CharField(max_length=20)
    # status_tittle = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return (self.body[0:20]) + '... by ' + self.user.username
    def get_url(self):
        return "/task%i" % self.id

