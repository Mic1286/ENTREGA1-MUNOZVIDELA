from django.db import models


# Create your models here.
class celulares (models. Model):
    marca= models.CharField (max_length=30)
    
    modelo= models.IntegerField ()
    
    precio= models.DateField ()
