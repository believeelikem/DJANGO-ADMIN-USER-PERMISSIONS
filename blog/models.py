from turtle import mode, title
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=224)
    
    def __str__(self):
        return self.title
    
    

