import datetime
from django.db import models

from django.utils import timezone

# Create your models here. Or edit, but remember always makemigration afer that
 
class Todo(models.Model):
    #Estos seran los atributos que llamaremos en los templates
    description = models.CharField(max_length=200)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    pub_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))

    class meta:
        ordering = ["-created"]

    def __str__(self):
        """This method returns the description when get the object"""
        return self.description
    
    