from rest_framework import serializers

from products.models import Product


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "image", "color", "price", "created_at"]