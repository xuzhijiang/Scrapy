# -*- coding: utf-8 -*-
import scrapy


class WebsiteGettingSpider(scrapy.Spider):
    name = 'website_getting'
    # start_urls = ['http://python123.io/ws/demo.html']

    def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = response.url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Save file: %s.' % file_name)