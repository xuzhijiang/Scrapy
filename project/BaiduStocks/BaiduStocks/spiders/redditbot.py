# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
	name = 'redditbot'
	allowed_domains = ['www.reddit.com/r/gameofthrones/']
	start_urls = ['https://www.reddit.com/r/gameofthrones/']

	def parse(self, response):
		# Extracting the content using css selector
		titles = response.css(".s5kz2p-0::text").extract()
		votes = response.css("._1rZYMD_4xY3gRcSS3p8ODO::text").extract()
		comments = response.css(".FHCV02u6Cp2zYL0fhQPsO::text").extract()
		rs = zip(titles, votes, comments)
		for item in rs:
			scraped_info = {
			  'title': item[0],
			  'vote': item[1],
			  'comment': item[2]
			}
			yield scraped_info
