#products app views 

from rest_framework import generics

from .models import Product
from .serializers import SerializerProduct


# generic API create an Product
class ProducCreateApiView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = SerializerProduct
  
  
# generic API
class ProducListApiView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = SerializerProduct


# generic API read an Product
class ProducDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = SerializerProduct