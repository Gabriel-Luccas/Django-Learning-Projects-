# products app views

from rest_framework import generics , permissions , authentication

from .models import Product
from .serializers import SerializerProduct


# generic API create an Product
class ProducCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct


# generic API delete an Product
class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    lookup_field = "pk"
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# generic API update an Product
class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    lookup_field = "pk"
    
    def perform_update(self, serializer):
      instance = serializer.save()


# generic list API
class ProducListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct


# generic API read an Product
class ProducDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
