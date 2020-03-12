from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

def generate_cube_id():
    return str(uuid.uuid4()).split("-")[-1]

class Cube(models.Model):
    cube_id = models.CharField(max_length=255, blank=True)
    cube = models.CharField(max_length=255)#each cube is length 182
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}".format(self.cube)
    
    
    def save(self, *args, **kwargs):
        if len(self.cube_id.strip(" "))==0:
            self.cube_id = generate_cube_id()
        
        super(Cube, self).save(*args, **kwargs)
        
    class Meta:    
        ordering = ["-created"]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name