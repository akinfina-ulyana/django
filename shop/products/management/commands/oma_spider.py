import requests
from products.models import Product
from products.spiders import OmaSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            image_name = item["image_name"].split("/")[-1]
            response = requests.get(item["image_name"])
            open(settings.MEDIA_ROOT / "products" / image_name, "wb").write(
                response.content
            )

            Product.objects.update_or_create(
                external_id=item["external_id"],
                defaults={
                    "title": item["name"],
                    "price": item["price"],
                    "image": f"products/{image_name}",
                    "excerpt": item["category"],
                    "description": item["link"],
                },
            )

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
