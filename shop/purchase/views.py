import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def purchase(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Shop purchases")
