#Importar nuestra clase viewset
from django.urls import path
from .views import ProductoDetalles, ProductoInfo, InfoNegocioDetalles, InfoNegocioInfo, DatosPedidoDetalles, DatosPedidoInfo, ItemsPedidoDetalle

urlpatterns = [
    path("Producto/",ProductoDetalles.as_view(), name="Producto"),
    path("Producto/<int:id>/",ProductoInfo.as_view()),
    path("InfoNegocio/",InfoNegocioDetalles.as_view()),
    path("InfoNegocio/<int:id>/", InfoNegocioInfo.as_view()),
    path("DatosPedido/", DatosPedidoDetalles.as_view()),
    path("DatosPedido/<int:id>/", DatosPedidoInfo.as_view()),
    path("ItemsPedido/", ItemsPedidoDetalle.as_view())
]