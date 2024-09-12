from rest_framework import serializers
from .models import Product


class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
        ]

"""    def validate_title(self, value):
        query_set = Product.objects.filter(title_iexpect=value)
        if query_set.exist():
            raise serializers.ValidationError(f" {value} is alredy a product name ")
        return value"""
