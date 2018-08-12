import scrapy


class ZipruSpider(scrapy.Spider):
	name = 'zipru'
	start_urls = ['http://zipru.to/torrents.php?category=TV']

	