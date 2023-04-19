from django.core.management.base import BaseCommand

from products.models import Product
from products.spiders import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            Product.objects.update_or_create(external_id=item["external_id"], defaults={
                "title": item["name"],
                "price": item["price"],
                "excerpt": item["category"],
                "description": item["link"],
            })
        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()