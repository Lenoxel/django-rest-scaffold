from django.db import models

class Client(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereço', max_length=100)
    idade = models.IntegerField('Idade')
    
    objects = models.Manager()

    def __str__(self):
        return self.name
    
