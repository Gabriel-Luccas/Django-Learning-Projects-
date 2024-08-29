#products app views 

from rest_framework import generics

from .models import Product
from .serializers import SerializerProduct


class ProducDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = SerializerProduct