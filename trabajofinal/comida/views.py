from rest_framework.views import APIView
from .models import Producto, InfoNegocio, DatosPedido, ItemsPedido
from .serializers import ProductoSerializer, InfoNegocioSerializer, DatosPedidoSerializer, ItemsPedidoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class ProductoDetalles(APIView):
   def get(self, request):
      obj = Producto.objects.all()
      serializer = ProductoSerializer(obj, many=True)      
      return Response(serializer.data, status=status.HTTP_200_OK)     

   def post(self, request):   
      serializer = ProductoSerializer(data=request.data)      

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)     
      else:                  
         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProductoInfo(APIView):
   def get(self, request, id):
      try:
         obj = Producto.objects.get(id=id)         

      except Producto.DoesNotExist:         
         msg={"msg":"Dato no existe..."}
         return Response(msg, status=status.HTTP_404_NOT_FOUND)

      serializer = ProductoSerializer(obj)
      return Response(serializer.data, status=status.HTTP_200_OK)        

   def put(self, request, id):
      try:
         obj = Producto.objects.get(id=id)

      except Producto.DoesNotExist:         
         return Response(serializer.data)

      serializer = ProductoSerializer(obj, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def patch(self, request, id):
      try:
         obj = Producto.objects.get(id=id)
                  
      except Producto.DoesNotExist:         
         return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

      serializer = ProductoSerializer(obj, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, id):
      try:
          obj = Producto.objects.get(id=id)
          obj.delete()
          return Response({"msg":"Eliminado..."}, status=status.HTTP_204_NO_CONTENT)
      except Producto.DoesNotExist: 
          msg = {"msg":"Dato no existe ..."}
          return Response(msg, status=status.HTTP_404_NOT_FOUND)

#----------------------------------------------------------------------------------------------------
class InfoNegocioDetalles(APIView):
   def get(self, request):
      obj = InfoNegocio.objects.all()
      serializer = InfoNegocioSerializer(obj, many=True)      
      return Response(serializer.data, status=status.HTTP_200_OK)     

   def post(self, request):   
      serializer = InfoNegocioSerializer(data=request.data)      

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)     
      else:                  
         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class InfoNegocioInfo(APIView):
   def get(self, request, id):
      try:
         obj = InfoNegocio.objects.get(id=id)         

      except InfoNegocio.DoesNotExist:         
         msg={"msg":"Dato no existe..."}
         return Response(msg, status=status.HTTP_404_NOT_FOUND)

      serializer = InfoNegocioSerializer(obj)
      return Response(serializer.data, status=status.HTTP_200_OK)        

   def put(self, request, id):
      try:
         obj = InfoNegocio.objects.get(id=id)

      except InfoNegocio.DoesNotExist:         
         return Response(serializer.data)

      serializer = InfoNegocioSerializer(obj, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def patch(self, request, id):
      try:
         obj = InfoNegocio.objects.get(id=id)
                  
      except InfoNegocio.DoesNotExist:         
         return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

      serializer = InfoNegocioSerializer(obj, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, id):
      try:
         obj = InfoNegocio.objects.get(id=id)
         obj.delete()
         return Response({"msg":"Eliminacion exitosa 👍"}, status=status.HTTP_204_NO_CONTENT)     

      except InfoNegocio.DoesNotExist: 
         msg = {"msg":"Dato no existe ..."}               
         return Response(msg, status=status.HTTP_404_NOT_FOUND)      

#----------------------------------------------------------------------------------------------------
class DatosPedidoDetalles(APIView):
   def get(self, request):
      obj = DatosPedido.objects.all()
      serializer = DatosPedidoSerializer(obj, many=True)      
      return Response(serializer.data, status=status.HTTP_200_OK)     

   def post(self, request):   
      serializer = DatosPedidoSerializer(data=request.data)      

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)     
      else:                  
         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DatosPedidoInfo(APIView):
   def get(self, request, id):
      try:
         obj = DatosPedido.objects.get(id=id)         

      except DatosPedido.DoesNotExist:         
         msg={"msg":"Dato no existe..."}
         return Response(msg, status=status.HTTP_404_NOT_FOUND)

      serializer = DatosPedidoSerializer(obj)
      return Response(serializer.data, status=status.HTTP_200_OK)        

   def put(self, request, id):
      try:
         obj = DatosPedido.objects.get(id=id)

      except DatosPedido.DoesNotExist:         
         return Response(serializer.data)

      serializer = DatosPedidoSerializer(obj, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def patch(self, request, id):
      try:
         obj = DatosPedido.objects.get(id=id)
                  
      except DatosPedido.DoesNotExist:         
         return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

      serializer = DatosPedidoSerializer(obj, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)     
      else:                  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, id):
      try:
         obj = DatosPedido.objects.get(id=id)
         obj.delete()
         return Response({"msg":"Eliminacion exitosa 👍"}, status=status.HTTP_204_NO_CONTENT)

      except DatosPedido.DoesNotExist: 
         msg = {"msg":"Dato no existe ..."}               
         return Response(msg, status=status.HTTP_404_NOT_FOUND) 
#----------------------------------------------------------------------------------------------------
class ItemsPedidoDetalle(APIView):
   def get(self, request):
      obj = ItemsPedido.objects.all()
      serializer = ItemsPedidoSerializer(obj, many=True)      
      return Response(serializer.data, status=status.HTTP_200_OK)     

   def post(self, request):   
      serializer = ItemsPedidoSerializer(data=request.data)      

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)     
      else:                  
         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



