# -*- coding: utf-8 -*-
import scrapy


class CatSpider(scrapy.Spider):
    name = 'cat'
    # allowed_domains = ['domain'] #[optional]
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s.' % fname)
