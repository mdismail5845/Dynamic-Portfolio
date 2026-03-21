from django.db import models

# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class ProjectSection(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField()
    
    def __str__(self):
        return self.title
    
class Projects(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)
    category =  models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    