from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.IntegerField(max_length=6)
	def __str__(self):
		return self.nombre

class Pedido(models.Model):
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(auto_now=True)
	productop = models.ForeignKey(Producto)
	cantidad = models.IntegerField(max_length=3)
