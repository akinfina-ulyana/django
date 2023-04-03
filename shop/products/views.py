
import logging
from django.http import HttpResponse
from django.shortcuts import render

from shop import settings
from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    # if request.GET.get("param"):
    #     logger.info(f"My param = {request.GET.get('param')}")
    #     logger.info(f"My custom variable = {settings.MY_CUSTOM_VARIABLE}")

    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__contains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    # string = "<br>".join([str(p) for p in products])
    # return HttpResponse(string)

    return render(request, "index.html", {"products": products})


# from shop.models import Product
#
# first_product = Product.objects.create(
#     title="First product", price=100
# )
