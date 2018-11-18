# -*- coding: utf-8 -*-
import scrapy
import logging


class AltexSpider(scrapy.Spider):
    name = 'altex'
    allowed_domains = ['altex.ro']
    start_urls = ['https://altex.ro/cafetiere/cpl/']

    def parse(self, response):
        items_xpath = response.xpath('//*[@class="Products-item"]')
        for item_xpath in items_xpath:
            title = item_xpath.xpath(
                './/*[@class="Product-list-right"]//@title'
            ).extract()
            url = item_xpath.xpath(
                './/*[@class="Product-list-right"]'
                '/*[@class="Product-nameHeading"]/a/@href'
            ).extract()
            reduction = item_xpath.xpath(
                './/*[@class="Badge-reducere"]/text()'
            ).extract()
            new_price = item_xpath.xpath(
                './/*[@itemprop="price"]/@content'
            ).extract()

            logging.info(
                "title: {0}, "
                "url: {1}, "
                "reduction: {2}, "
                "new_price: {3}, "
                .format(title, url, reduction, new_price)
            )
