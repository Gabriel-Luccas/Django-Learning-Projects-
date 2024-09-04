from rest_framework import viewsets

from .models import Product
from .serializers import SerializerProduct


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    lookup_field = "pk"
