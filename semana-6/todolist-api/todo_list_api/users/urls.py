# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()

# # Se tiene que registrar las rutas

# router.register (r'users', UserViewSet)

# urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthenticationView
from django.urls import path


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'login', AuthenticationView.as_view(), name='custom_login'),
    *router.urls
]