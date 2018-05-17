# -*- coding: utf-8 -*-
import scrapy


class CatSpider(scrapy.Spider):
    name = 'cat'
    # allowed_domains = ['domain'] #[optional]
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        file_name = response.url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s.' % file_name)
