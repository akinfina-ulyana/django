from decimal import Decimal

import requests
from django_rq import job
from products.models import Product

from django.core.management.base import BaseCommand


@job
def update_products():
    response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
    result = response.json()
    item = None
    for item in result:
        if item["Cur_Abbreviation"] == "USD":
            break

    if item is not None:
        for products in Product.objects.all():
            products.price_usd = products.price / Decimal(item["Cur_OfficialRate"])
            products.save()


class Command(BaseCommand):
    help = "update products"

    def handle(self, *args, **options):
        update_products()
