from django.contrib import admin
from .models import Producto, InfoNegocio, DatosPedido, ItemsPedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo','descripcion','precio']
    search_fields = ('titulo','descripcion','precio')

@admin.register(DatosPedido)
class DatosPedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombres','apellido','fechaHora','totalPedido','pedidoatendido','fechaHoraAtendido']
    list_editable = ['pedidoatendido','fechaHoraAtendido']

    search_fields = ('nombres','apellido','direccion')

@admin.register(ItemsPedido)
class ItemsPedidoAdmin(admin.ModelAdmin):
    #list_display = ['id','cantidad','productostitulo','datosPedidoIdnombres', 'datosPedidoIdapellido']
    list_display = ['id','cantidad', 'productostitulo', 'createt_at', 'datosPedidoIdnombres','datosPedidoIdapellido']

    def productostitulo(self, obj):
        return obj.productoId.titulo
    productostitulo.short_description = 'Producto'

    def datosPedidoIdnombres(self, obj):
         return obj.datosPedidoId.nombres
    datosPedidoIdnombres.short_description = 'Nombres'

    def datosPedidoIdapellido(self, obj):
         return obj.datosPedidoId.apellido
    datosPedidoIdapellido.short_description = 'Apellido'



admin.site.register(InfoNegocio)
admin.site.site_header  ="Red Burguer"

# admin.site.index_header =""
# admin.site.site_title  = ""

#admin.site.register(Producto)
#admin.site.register(DatosPedido)
#admin.site.register(ItemsPedido)



