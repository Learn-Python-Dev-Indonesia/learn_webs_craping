"""
Daftar Pusat UTBK  TUNA NETRA : PTN 2022
"""
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://ltmpt.ac.id/?mid=22',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for i in range (1, 75):
       # for sekolah in response.css('.table > tbody:nth-child(2)'):
            yield {
                'Nomer' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
            }
# .col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5)