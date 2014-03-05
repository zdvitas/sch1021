from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    cabinet = models.CharField(max_length=20)


class Task(models.Model):
    tittle = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(CustomUser)
    def __unicode__(self):
        return self.title + ' by ' + self.user.username
    def get_url(self):
        return "/task%i" % self.id

