from django.db import models
from decimal import Decimal

COLOR_CHOICES = (
    ("RED", "red"),
    ("GREEN", "green"),
    ("BLUE", "blue"),
)


class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default="RED")
    price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=5, max_digits=10
    )
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Product : {self.title} - {self.price}"
