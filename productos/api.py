from productos.models import Productos
from rest_framework import viewsets, permissions
from .serializers import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosSerializer
    