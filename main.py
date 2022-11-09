"""
Ini berkas scraping mengunakan plugin scrapy, tetapi belum bisa cetak sampai file csv
"""
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range (1, 101):
            for sekolah in response.css('.table > tbody:nth-child(2)'):

                yield {
                    'Rangking' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
                    'NPSN' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(3)::text').extract(),
                    'nama_sekolah' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(4)::text').extract(),
                    'Nilai_Total' : sekolah(' tr:nth-child('+ str(i) +') > td:nth-child(5)::text').extract(),
                    'Provinsi' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(6)::text').extract(),
                    'Kabupaten' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(7)::text').extract(),
                    'Jenis' : sekolah('tr:nth-child('+ str(i) +') > td:nth-child(8)::text').extract()
                }

# Nama Sekolahan
# .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)
# .table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4)
#Nomer Urut
# .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
# Jenis hal 1
#.table > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(8)
# .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8)

# nomer 101
# .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)
# nomer 102
# .table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4)