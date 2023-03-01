from django.contrib import admin

from purchase.models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ("user", "product", "count", "created_at")
   fields = ("user", "product", "count", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("user__email", "product__title")

