from django.http import JsonResponse
import json

from products.models import Product


def api_home(request, *args, **kwargs):
    all_products = Product.objects.all()
    data  = json.loads(all_products)
    return JsonResponse(data)
