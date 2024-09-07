from django.db import models

# Create your models here.

class PageVisit(models.Model):
    #dp -> table
    #id -> hidden -> primary key -> auto increment
    path = models.TextField(null=True, blank=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col
