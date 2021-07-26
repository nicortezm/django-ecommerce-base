from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField("nombre producto",max_length=200,unique=True)
    imagen = models.ImageField(upload_to='productos/',blank=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre