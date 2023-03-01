import logging
from django.http import HttpResponse
from shop import settings

logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
        logger.info(f"My custom variable = {settings.MY_CUSTOM_VARIABLE}")
    return HttpResponse("Shop index view")


# from shop.models import Product
#
# first_product = Product.objects.create(
#     title="First product", price=100
# )
