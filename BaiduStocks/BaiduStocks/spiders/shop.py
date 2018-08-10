# -*- coding: utf-8 -*-
import scrapy


class ShopSpider(scrapy.Spider):
	name = 'shop'
	allowed_domains = ['http://192.168.6.1:8080/shop.html']
	start_urls = ['http://http://192.168.6.1:8080/shop.html/']
	custom_settings = {
		'FEED_URL': 'tmp/shop.csv'
	}

	def parse(self, response):
		#Extract product information
	   titles = response.css('img::attr(title)').extract()
	   #images = response.css('img::attr(data-img)').extract()
	   prices = response.css('.p_price::text').extract()
	   discounts = response.css('.prd_discount::text').extract()


	   for item in zip(titles,prices,discounts):
		   scraped_info = {
			   'title' : item[0],
			   'price' : item[1],
			   # 'image_urls' : [item[2]], #Set's the url for scrapy to download images
			   'discount' : item[2]
		   }

		   yield scraped_info
