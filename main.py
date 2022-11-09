"""
Ini berkas scraping mengunakan plugin scrapy, dengan output file csv
"""
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=3&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=4&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=5&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=6&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=7&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=8&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=9&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=10&per-page=100',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for i in range (1, 101):
       # for sekolah in response.css('.table > tbody:nth-child(2)'):
            yield {
                'Rangking' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
                'NPSN' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(3)::text').extract(),
                'nama_sekolah' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(4)::text').extract(),
                'Nilai_Total' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(5)::text').extract(),
                'Provinsi' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(6)::text').extract(),
                'Kabupaten' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(7)::text').extract(),
                'Jenis' : response.css('tr:nth-child('+ str(i) +') > td:nth-child(8)::text').extract()
            }
#cara run : scrapy runspider main.py
#unduh file csv : scrapy runspider main.py -O lmptm.py
