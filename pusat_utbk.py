"""
Daftar Pusat UTBK PTN 2022
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
        for sekolah in response.css('col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1)'):
            for i in range(1, 75):
                yield {
                    'Nomer' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
                    'Kode' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(2)::text').extract(),
                    'Nama' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(3)::text').extract(),
                    'Alamat' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(4)::text').extract(),
                    'Kode Pos' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(5)::text').extract(),
                    'No Telpon' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(6)::text').extract(),
                    'Email' : sekolah.css('tr:nth-child('+ str(i) +') > td:nth-child(7)::text').extract(),
                }
# .col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5)