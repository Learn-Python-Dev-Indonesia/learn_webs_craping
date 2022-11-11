"""
Daftar PTN
"""
import scrapy

class PTN(scrapy.Spider):
    name = "PTN"
    start_urls = ['https://sidata-ptn.ltmpt.ac.id/ptn_sn.php?']


    def parse(self, response):

        for universitas in response.css('table > tbody:nth-child(2) > tr'):

            yield {
                'Nomer' : universitas.css('td:nth-child(1)::text').extract(),
                'Kode' : universitas.css('td:nth-child(2) > a:nth-child(1)::text').extract(),
                'Nama_Universitas' : universitas.css('td:nth-child(3) > a:nth-child(1)::text').extract(),
                'URL_Universitas' : universitas.css('td:nth-child(3) > a:nth-child(3)::text').extract(),
            }
    # .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
# 1 .table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > a:nth-child(1)
# 2 .table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3) > a:nth-child(1)