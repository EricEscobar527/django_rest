from rest_framework import routers
from .api import ProductosViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductosViewSet, 'productos')

urlpatterns = router.urls
