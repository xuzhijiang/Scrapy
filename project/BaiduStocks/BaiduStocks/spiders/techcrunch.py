# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpider(scrapy.Spider):
	#name of the spider
	name = 'techcrunch'

	#list of allowed domains
	allowed_domains = ['techcrunch.com/feed/']

	#starting url for scraping
	start_urls = ['http://techcrunch.com/feed/']

	#setting the location of the output csv file
	custom_settings = {
		'FEED_URI' : 'tmp/techcrunch.csv'
	}

	def parse(self, response):
		#Remove XML namespaces
		#'dc:' and '![CDATA' are just XML namespace, so we delete it using method below.
		response.selector.remove_namespaces()

		#Extract article information
		#Notice that text() here is equivalent to ::text from css selector.
		titles = response.xpath('//item/title/text()').extract()

		authors = response.xpath('//item/creator/text()').extract()
		dates = response.xpath('//item/pubDate/text()').extract()
		links = response.xpath('//item/link/text()').extract()

		for item in zip(titles,authors,dates,links):
			scraped_info = {
				'title' : item[0],
				'author' : item[1],
				'publish_date' : item[2],
				'link' : item[3]
			}

			yield scraped_info