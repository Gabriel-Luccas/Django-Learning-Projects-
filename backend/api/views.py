
from django.forms.models import model_to_dict  # Convert a model to a dict
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import SerializerProduct

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # Corrigido: Itera sobre o QuerySet e converte cada objeto para um dicionário
    if instance:
        #data = model_to_dict(instance)
        data = SerializerProduct(instance).data
    # Retorna a lista de produtos como JSON
    return Response(data)  # `safe=False` permite retornar uma lista