from django.db import models

# Create your models here.
class SignUp(models.Model):
    correo = models.EmailField()
    full_name = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    #auto_now_add   cada vez que se agregue automaticamente se agrega la fecha
    #auto_now       cada vez que se modifica se agrega la fecha

    def __unicode__(self):  #PYTHON 3.3 is __str__
        return self.correo

#CADA vez que se modifica el models.py se debe ser un makemigrations
#