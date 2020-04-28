# -*- coding: utf-8 -*-
import scrapy


class MySpider(scrapy.Spider):
    name = 'getmoney'
    #allowed_domains = ['https://www.fundamentus.com.br/index.php']
    start_urls = ['https://www.fundamentus.com.br/detalhes.php?papel=ITSA4',
	        	]

    def parse(self, response):

    	for data in response.css('span.txt'):
    		yield{
    			'data': data.css('::text').get(),
    		}
        

if __name__ == "__main__":
	crawler = MySpider() 