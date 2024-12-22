from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scrap_jobs.scrap_jobs.spiders.job_spider import JobSpider

def run_spider(start_url):
    process = CrawlerProcess(get_project_settings())
    scraped_data = []

    def collect_results(item, response, spider):
        scraped_data.append(item)

    # Connect the signal to collect scraped items
    from scrapy import signals
    process.crawl(JobSpider, start_url=start_url)
    crawler = list(process.crawlers)[0] if process.crawlers else None
    if crawler:
        crawler.signals.connect(collect_results, signal=signals.item_scraped)

    # Start the spider
    process.start()

    return scraped_data
