from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet

router = DefaultRouter()

# Se tiene que registrar las rutas

router.register (r'categories', CategoryViewSet)
router.register (r'task', TaskViewSet)

urlpatterns = router.urls