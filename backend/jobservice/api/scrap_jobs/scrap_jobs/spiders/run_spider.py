from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .job_spider import JobSpider

# Function to run the spider
def run_spider():
    process = CrawlerProcess(get_project_settings())

    # Start the spider with a custom start URL
    process.crawl(JobSpider, start_url="https://www.dice.com/jobs?q=Software&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en")
    
    # Start the crawling process
    process.start()


