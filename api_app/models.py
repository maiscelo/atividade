from django.db import models

# Create your models here.
from django.db import models

class objeto_tipo(models.Model):
    tipo = models.CharField(max_length=200)

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
# travessa belhorizonte 40  986948596 jr da suzete

class Arma(models.Model):
   marca = models.CharField(max_length=200)
   modelo = models.CharField(max_length=200)
   quantidade_de_tiros = models.PositiveIntegerField()
   valor_estimado = models.PositiveIntegerField()
   #imagem =

class Monicao(models.Model):
   marca = models.CharField(max_length=200)
   modelo = models.CharField(max_length=200)
   valor_estimado = models.PositiveIntegerField()


#valor_estimado = models.PositiveIntegerField(choices=((33,"33"),(55,"55"),(4,"4")))
"""
class Model(model.Model):
    field1=models.CharField()
    field2=models.CharField()
    field3=models.CharField()

    def myfunc (self):
    pass

        #
    def save(self, *args, **kwargs):
        q =  MyModel.objects.select_related('fields1', 'field2',  'filed2').filter(related_field)
    super(Model, self).save(*args, **kwargs)
"""
