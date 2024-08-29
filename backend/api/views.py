#API app views

from django.forms.models import model_to_dict  # Convert a model to a dict
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import SerializerProduct

from products.models import Product


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = SerializerProduct(request.data)
    if serializer.is_valid():
        data = serializer.data
        return Response(data)  # `safe=False` permite retornar uma lista
