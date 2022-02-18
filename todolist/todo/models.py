import datetime
from django.db import models

from time import timezone

# Create your models here. Or edit, but remember always makemigration afer that
 
class Todo(models.Model):
    #Estos seran los atributos que llamaremos en los templates
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """This method returns the description when get the object"""
        return self.description
    
    def was_published_recently(self):
        """This method show us true or false if the Todo was recently published"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    