import scrapy
import pandas as pd

class BrickSetSpider(scrapy.Spider):
	#name = "brickset_spyder"
	#start_urls = ['http://brickset.com/sets/year-2016']

	# new test
	name = 'aliexpress_tablets'
	allowed_domains = ['aliexpress.com']
	stat_urls = ['https://www.aliexpress.com/category/200216607/tablets.html',
                 'https://www.aliexpress.com/category/200216607/tablets/2.html?site=glo&g=y&tag=']

	def parse(self, response):

		print("\033[32m ********processing \033[37m")

		# Extracting the data using css selector
		product_name = response.css('.product::text').extract_first()
		price_range = response.css('.value::text').extract_first()
		
		# 
		orders = response.xpath("//em[@title='Total Orders']/text()").extract()
		company_name = response.xpath("//a[@class='store $p4pLog']/text()").extract()

		row_data = zip(product_name, price_range, orders, company_name)

		for item in row_data:
			scraped_info = {
				'page': response.url,
				'product_name':item[0],
				'price_range':item[1],
				'orders': item[2],
				'company_name': item[3],
			}
		
		yield scraped_info
			
		data = pd.DataFrame(scraped_info)
		data.to_csv('/home/gustavo/Documentos/ShowOff/test.csv',index=False)
		#SET_SELECTOR = '.set' # class that we want
		'''
			

	def parse(self, response):
		for quote in response.css('div.quote'):
			
			yield {
				'text': quote.css('span.text::text').get(),
				'author': quote.css('small.author::text').get(),
				'tags': quote.css('div.tags a.tag::text').getall(),
			}


		'''