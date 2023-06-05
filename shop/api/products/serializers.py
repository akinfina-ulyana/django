from rest_framework import serializers

from products.models import Product


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    has_image = serializers.SerializerMethodField()
    purchases_count = serializers.IntegerField()
    purchases_total = serializers.IntegerField()

    def get_has_image(self, obj: Product) -> bool:
        return bool(obj.image)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "has_image",
            "purchases_count",
            "purchases_total",
            "image",
            "color",
            "price",
            "created_at",
        ]
