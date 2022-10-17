from pyexpat import model
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class demoModel( models.Model):
    name = models.CharField( max_length = 50)

    def __str__(self):
        return self.name
