from django.urls import path
from rest_framework import routers
from .api import ProductosViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

router = routers.DefaultRouter()
router.register('api/productos', ProductosViewSet, 'productos')

urlpatterns = [
    *router.urls,
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
