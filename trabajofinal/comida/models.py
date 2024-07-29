from django.db import models
from datetime import datetime

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.TextField()
    precio = models.FloatField(blank=False, null=False)
    imagen = models.CharField(max_length=250, blank=False, null=False)
    
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        # return self.titulo +' - '+self.descripcion+' - '+str(self.precio)
        return self.titulo +' - '+str(self.precio)

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ["titulo"]     


class InfoNegocio(models.Model):
    titulo = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    horario = models.CharField(max_length=150, null=True, blank=True)
    
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        db_table = 'negocio'
        verbose_name = 'Dato del Negocio'
        verbose_name_plural = 'Datos del Negocio'        

class DatosPedido(models.Model):
    nombres     = models.CharField(max_length=100, null=True, blank=True)
    apellido    = models.CharField(max_length=100, null=True, blank=True)
    direccion   = models.CharField(max_length=250, null=True, blank=True)
    phone       = models.CharField(max_length=30,  null=True, blank=True)
    referencia  = models.TextField(null=True, blank=True)
    email       = models.CharField(max_length=150, null=True, blank=True)
    totalPedido = models.FloatField()
    fechaHora   = models.DateTimeField(null=True)
    totalItems  = models.IntegerField()
    pedidoatendido  = models.BooleanField(null=True)
    fechaHoraAtendido = models.DateTimeField(null=True)
        
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self) -> str:
        datofecha=self.fechaHora.strftime('%m/%d/%Y, %H:%M:%S')        
        return self.nombres+'-'+self.apellido+'-'+datofecha

    class Meta:
        db_table = 'datospedidos'
        verbose_name = 'Atencion de Pedido'
        verbose_name_plural = 'Atencion de Pedidos'
        ordering = ["-id"]     

class ItemsPedido(models.Model):
    productoId = models.ForeignKey(
        Producto, related_name='productos', on_delete = models.CASCADE)

    datosPedidoId = models.ForeignKey(
        DatosPedido, related_name='datospedidos', on_delete = models.CASCADE)

    cantidad = models.IntegerField()
    precio   = models.FloatField()
    total    = models.FloatField()

    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
         datofecha=self.datosPedidoId.fechaHora.strftime('%m/%d/%Y, %H:%M:%S')
         cantidax= str(self.cantidad)
         return cantidax+' - '+self.productoId.titulo+' - '+self.datosPedidoId.nombres+' '+self.datosPedidoId.apellido+' - '+datofecha
        
         
    class Meta:
        db_table = 'itemspedidos'
        verbose_name = 'Pedido Realizado'
        verbose_name_plural = 'Pedidos Realizados'
        ordering = ["-id"]        


   