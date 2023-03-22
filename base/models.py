from django.db import models

# Create your models here.

class room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # particpants = 
    updateD = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    kosalghba = models.TextField(auto_created=True)
    
    def __str__(self):
        return self.name