from api.products.serializers import ProductModelSerializer
from products.models import Product
from rest_framework import viewsets

from django.db.models import Count, Sum


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = (
        Product.objects.annotate(purchases_count=Count("purchases"))
        .annotate(purchases_total=Sum("purchases__count"))
        .order_by("-created_at")
    )

    serializer_class = ProductModelSerializer
    permission_classes = []
