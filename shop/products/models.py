from django.db import models

COLOR_CHOICES = (
    ("RED", "red"),
    ("GREEN", "green"),
    ("BLUE", "blue"),
)




class Product(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default="RED")
    price = models.IntegerField(default=0)
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Product : {self.title} - {self.price}"

