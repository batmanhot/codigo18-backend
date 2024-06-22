
#Importar nuestra clase viewset
from .views import ProductViewSet, CategoryViewSet

#Importar el router de DRF (django rtest Framework)
from rest_framework.routers import DefaultRouter

#crear una instancia
router = DefaultRouter()

#agregar una ruta usando router
router.register(r'products',ProductViewSet)
router.register(r'categories',CategoryViewSet)

urlpatterns = router.urls



