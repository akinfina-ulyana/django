from profiles.models import Address, Profile

from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    fields = ("user", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "address", "created_at")
    fields = ("user", "country", "city", "address", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("country", "city")


# user = models.ForeignKey(
#    settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses"
# )
# country = models.CharField(max_length=255)
# city = models.CharField(max_length=255)
# address = models.CharField(max_length=255)
# created_at = models.DateTimeField(
#    auto_now_add=True, db_index=True
# )
