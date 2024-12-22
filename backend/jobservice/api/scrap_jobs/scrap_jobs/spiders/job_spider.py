import scrapy

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    url = 'https://www.dice.com/jobs?q=Software&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en'

    def __init__(self, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url', self.url)]

    def parse(self, response):
        self.logger.info(f"Crawling URL: {response.url}")
        
        job_cards = response.css(".card-title-link")

        title = response.xpath('//a[contains(@class , "card-title-link")]')
        print('title :' , title , job_cards)
        if not job_cards:
            self.logger.warning("No job cards found")
        
        for job in job_cards:
            title = job.xpath('.//a[contains(@class, "card-title-link")]/text()').get()
            job_link = job.xpath('.//a[contains(@class, "card-title-link")]/@href').get()

            if title and job_link:
                self.logger.info(f"Job title: {title}")
                self.logger.info(f"Job link: {job_link}")
                
                yield response.follow(job_link, callback=self.parse_job_detail, meta={'job_title': title})

    def parse_job_detail(self, response):
        job_title = response.meta['job_title']
        job_description = response.xpath('//div[@class="job-description"]//text()').getall()
        job_description = ' '.join(job_description).strip()
        
        yield {
            'job_title': job_title,
            'job_description': job_description,
            'job_link': response.url,
        }
