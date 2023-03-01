from django.conf import settings
from django.db import models

class Purchase(models.Model):
   user = models.ForeignKey(
       settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
   )
   product = models.ForeignKey(
       "products.Product", on_delete=models.CASCADE, related_name="purchases"
   )
   count = models.IntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True, db_index=True)



   #products.models