from django.contrib import admin

from products.models import Product
from purchase.models import Purchase

class PurchaseInline(admin.TabularInline):
   model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("title", "price", "description", "color", "created_at")
   fields = ("title", "price", "description", "color", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("title", "description")
   inlines = [
      PurchaseInline,
   ]
















