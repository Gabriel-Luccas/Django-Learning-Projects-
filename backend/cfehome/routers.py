"""from rest_framework.routers import DefaultRouter
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


from products.viewset import ProductViewSet

router = DefaultRouter()
router.register("products-abc", ProductViewSet, basename="products")


urlpatterns = router.urls
"""